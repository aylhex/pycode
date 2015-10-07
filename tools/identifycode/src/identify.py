# coding=utf-8
import sys
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw
from StringIO import StringIO
import copy
import json

from collectfont import show,showchar_dict


# 加载字模数据
with open('data.json') as f:
    CharMatrix = json.loads(f.read())

# the num of chars
charnum = 5  
# start postion of first number
xstart = 6
# width of each number
xwidth = 9
# start postion of top 
ystart = 5
# height of each number
yhigh = 13  

def ImgFilter(image_name):
    im = Image.open(image_name)
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    # im.show()
    return im

# 计算阀值
def calcThreshold(img):
    im = Image.open(img)
    L = im.convert('L').histogram()
    num = 0
    threshold = 0
    for i in xrange(len(L)):
        num += L[i]
        if num >= 530:
            threshold = i
            break
    return threshold

# 二值化
def binaryzation(img, threshold=110):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    if not isinstance(img, StringIO) and type(img) != str and type(img) != unicode:
        raise Exception('img must be StringIO or filename(str/unicode)')
    im = Image.open(img)
    imgry = im.convert('L')
    imgry.save("bi0.bmp")
    imout = imgry.point(table, '1')
    imout.save("bi.bmp")
    return imout

# split five numbers in the picture
def CropPic(im):
    im_crop_list = []
    # cut every char
    for i in range(charnum):
        im1 = im.crop((xstart+xwidth*i, ystart, xstart+xwidth*(i+1), ystart+yhigh))
        im_crop_list.append(im1)
    return im_crop_list

# 抽取出字符矩阵 列表
def extractChar(im):
    """
    返回列表，每个元素为对应黑块的信息字典
    """    
    # 坐标偏移,对应周围八个像素
    # OFFSETLIST = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    OFFSETLIST = [(1, 0), (0, 1), (-1, 0), (0, -1),]
    # 设置阀值，色块内的像素数目
    filter_num=20

    pixelAccess = im.load()
    # 图片中黑块个数
    num = 1
    # 黑点坐标临时队列
    queue = []
    # 初始化一个与图片长宽相等的矩阵
    ff = [[0]*im.size[1] for i in xrange(im.size[0])]

    # floodfill 提出黑色块,包括噪点
    for i in xrange(im.size[0]):
        for j in xrange(im.size[1]):
            # pixelAccess[i,j] == 0 表示是黑点
            if pixelAccess[i, j] == 0 and ff[i][j] == 0:
                ff[i][j] = num
                queue.append((i, j))
                while len(queue) > 0:
                    a, b = queue[0]
                    queue = queue[1:]
                    for offset1, offset2 in OFFSETLIST:
                        x, y = a + offset1, b + offset2
                        if x < 0 or x >= im.size[0]:
                            continue
                        if y < 0 or y >= im.size[1]:
                            continue
                        if pixelAccess[x, y] == 0 and ff[x][y] == 0:
                            ff[x][y] = num
                            queue.append((x, y))
                # 遍历完一个字符的像素，num加1
                num += 1

    # 字符点阵的坐标列表，对齐到 (0,0)
    # eg: [(1,2),(3,24),(54,23)]
    # 初始化字符数组
    info = {
        "x_min": im.size[0],
        "y_min": im.size[1],
        "x_max": 0,
        "y_max": 0,
        "width": 0,
        "height": 0,
        "number": 0,
        "points": []
    }
    charList = [copy.deepcopy(info) for i in xrange(num)]
    # 遍历ff，统计黑点，并更新charList列表
    for i in xrange(im.size[0]):
        for j in xrange(im.size[1]):
            if ff[i][j] == 0:
                continue
            # 从ff数组中获取黑色块的序号
            black_id = ff[i][j]
            # 此处还有疑问，black_id和charList序号对不上
            # black_id是从1开始的
            # 此处得到每个黑色块的x,y轴最小/大值
            if i > charList[black_id]['x_max']:
                charList[black_id]['x_max'] = i
            if j > charList[black_id]['y_max']:
                charList[black_id]['y_max'] = j
            if i < charList[black_id]['x_min']:
                charList[black_id]['x_min'] = i
            if j < charList[black_id]['y_min']:
                charList[black_id]['y_min'] = j
            charList[black_id]['number'] += 1
            charList[black_id]['points'].append((i, j))
    # 不以(0,0)为原点了，而是以(x_min,y_min)为原点
    for i in xrange(num):
        charList[i]['width'] = charList[i]['x_max'] - charList[i]['x_min'] + 1
        charList[i]['height'] = charList[i]['y_max'] - charList[i]['y_min'] + 1
        # 修正偏移
        charList[i]['points'] = [(x-charList[i]['x_min'], y-charList[i]['y_min']) for x, y in charList[i]['points']]
    # 过滤杂点
    # ret = [one for one in charList if one['number'] > filter_num]
    ret = filter(lambda item:item['number']>filter_num, charList)
    # 排序
    ret.sort(lambda a, b: a['x_min'] < b['x_min'])
    return ret

# 识别字符
def charSimilarity(charA, charB):
    # charA  从图片中提取出来的数据
    # charB  字模中的数据
    # 对字模进行处理：去重，转成元组
    s2 = set([(one[0], one[1]) for one in charB['points']])
    sumlen = len(charA['points']) + len(charB['points'])
    num_max = 0
    # 晃动匹配
    # 计算出字模是否比图片中的字符宽(长)
    i_adjust = 1 if charB['width'] - charA['width'] >= 0 else -1
    j_adjust = 1 if charB['height'] - charA['height'] >= 0 else -1
    for i in xrange(0, charB['width'] - charA['width'] + i_adjust, i_adjust):
        for j in xrange(0, charB['height'] - charA['height'] + j_adjust, j_adjust):
            s1 = set([(one[0]+i, one[1]+j) for one in charA['points']])
            sim = len(s1 & s2) * 2.0 / sumlen
            if sim > num_max:
                num_max = sim
    return num_max

# 识别字符
def recognise(dict_char):
    num_max = 0
    ret = None
    for char in CharMatrix:
        s = charSimilarity(dict_char, CharMatrix[char])
        # print s * 100,"%"
        if s > num_max:
            ret = char
            num_max = s
    return ret


# 识别验证码主函数
def DoWork(img):
    ans = []
    threshold = calcThreshold(img)
    print 'threshold:', threshold
    im = binaryzation(img, threshold)
    chars = extractChar(im)
    for one in chars:
        ans.append(recognise(one))
    return ans

# 获取字模
def dump(char, dic):
    with open('../json/' + char + '.json', 'wb') as f:
        f.write(json.dumps(dic))

def GETSTAND():
    ans = []
    picpath = '../pic/25470.jpg'
    im = binaryzation(picpath)
    for one in extractChar(im):
        ans.append(one)
    print 'LAST:', len(ans)
    if len(ans) != 5:
        print '!!!!!!!!!!! ERROR !!!!!!!!!!!!!'
    else:
        # dump('K',ans[0])
        # dump('_k',ans[1])
        dump('Z', ans[2])
        # dump('Y',ans[3])
        # dump('K',ans[4])


def test():
    fpath='../pic/55154.jpg'
    tempnum=calcThreshold(fpath)
    im=binaryzation(fpath)
    im.show()
    im_crop_list=CropPic(im)
    for item in im_crop_list:
        dict_char=extractChar(item)[0]
        print "========"
        showchar_dict(dict_char)
        print "result:",recognise(dict_char)

def main():
    if len(sys.argv)==2:
        char=sys.argv[1]
        show(char)
    else:
        test()

if __name__ == '__main__':
    main()
