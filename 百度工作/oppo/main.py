import os
import sys
import threading
import time
import config
import pygame

def chick_postion(x, y):
    """
    点击对应坐标
    :param x: 横坐标
    :param y: 纵坐标
    :return: none
    """
    # os.system('adb -s c5eec105 shell input tap {} {}'.format(x, y))
    os.system('adb -s {} shell input tap {} {}'.format(config.PHONE_ID, x, y))


def swipe_postion(x1, y1, x2, y2):
    """
    点击x1,y1,并滑动手机到坐标x2,y2
    :param x1: 起始位置x坐标
    :param y1: 起始位置y坐标
    :param x2: 终点位置x坐标
    :param y2: 终点位置y坐标
    :return: none
    """
    os.system('adb -s {} shell input swipe {} {} {} {}'.format(config.PHONE_ID, x1, y1, x2, y2))


def long_postion(x1, y1, times):
    """
    点击x1,y1,并滑动手机到坐标x2,y2
    :param x1: 起始位置x坐标
    :param y1: 起始位置y坐标
    :param x2: 终点位置x坐标
    :param y2: 终点位置y坐标
    :return: none
    """
    # print('adb -s {} shell input swipe {} {} {} {} {}'.format(config.PHONE_ID, x1, y1, x1, y1, times))
    os.system('adb -s {} shell input swipe {} {} {} {} {}'.format(config.PHONE_ID, x1, y1, x1, y1, times))


def iphone_reboot():
    """
    chongqi
    :return:
    """
    os.system('adb -s {} reboot'.format(config.PHONE_ID))


def get_keyword_postion(model, key):
    """
    获取对应字母坐标
    :param model: 面板
    :param key: 想要获取的面板对应的字母或数字等的坐标
    :return: 坐标
    """
    phone_type = config.PHONE_TYPE
    for keyword, postion in config.data[phone_type][model].items():
        if key in keyword:
            return postion
    else:
        return [0, 0]


def get_hw_postion(model, key):
    phone_type = config.PHONE_TYPE
    for keyword, postion_list in config.data[phone_type][model].items():
        if key == keyword:
            return postion_list
    else:
        return False


def from_keys_long_chick(model, keys, times, isone=False):
    if isone:
        keys = [keys]
    for key in keys:
        x, y = get_keyword_postion(model, key)
        if x != 0 and y != 0:
            t = threading.Thread(target=long_postion, args=(x, y, times))
            t.start()
            time.sleep(0.25)
        else:
            print("没有找到{}下的{},暂不点击".format(model, key))


def form_keys_chick(model, keys, isone=False):
    """
    遍历输入内容进行点击
    :param model:
    :param keys:
    :return:
    """
    if isone:
        keys = [keys]
    for key in keys:
        x, y = get_keyword_postion(model, key)
        if x != 0 and y != 0:
            t = threading.Thread(target=chick_postion, args=(x, y))
            t.start()
            time.sleep(0.25)
        else:
            print("没有找到{}下的{},暂不点击".format(model, key))


def hw_data(model, key, isone=False):
    if isone:
        form_keys_chick(model, key, isone)
        return
    postion_list = get_hw_postion(model, key)
    for postions in postion_list:
        if len(postions) == 2:
            t = threading.Thread(target=swipe_postion, args=(*postions[0], *postions[1]))
            t.start()
            time.sleep(1)
        else:
            print("没有找{}下的{},暂不点击,返回为{}".format(model, key, postion_list))


def py9_case_oppo():
    for i in range(5):
        for j in range(10):
            form_keys_chick("py9", "quyuan")
            form_keys_chick("py9", "space", isone=True)
            form_keys_chick("py9", "pengyou")
            form_keys_chick("py9", "space", isone=True)
            form_keys_chick("py9", "rangwo")
            form_keys_chick("py9", "space", isone=True)
            form_keys_chick("py9", "pianyi")
            form_keys_chick("py9", "space", isone=True)
        print("第{}次执行结束等5S".format(i))
        time.sleep(5)
    print("{}执行结束".format(sys._getframe().f_code.co_name))


def py26_case_oppo():
    for i in range(5):
        for j in range(10):
            form_keys_chick("py26", "jintiantianqibucuo", )
            form_keys_chick("py26", "space", isone=True)
        print("第{}次执行结束等5S".format(i))
        time.sleep(5)
    print("{}执行结束".format(sys._getframe().f_code.co_name))


def en26_case_oppo():
    for i in range(5):
        for j in range(10):
            form_keys_chick("en26", "congratulation")
            form_keys_chick("en26", "space", isone=True)
        print("第{}次执行结束等5S".format(i + 1))
        time.sleep(5)
    print("{}执行结束".format(sys._getframe().f_code.co_name))


def bh_case_oppo():
    for i in range(5):
        for j in range(10):
            form_keys_chick("bh9", "123452")
            form_keys_chick("bh9", "space", isone=True)
        print("第{}次执行结束等5S".format(i + 1))
        time.sleep(5)
    print("{}执行结束".format(sys._getframe().f_code.co_name))


def hw_case_oppo():
    for i in range(5):
        for j in range(10):
            hw_data("hw", "one")
            hw_data("hw", "space", isone=True)
        print("第{}次执行结束等5S".format(i + 1))
        time.sleep(5)
    print("{}执行结束".format(sys._getframe().f_code.co_name))


def py9_en26_swich_oppo():
    for i in range(5):
        for j in range(10):
            form_keys_chick("py9", "ch", isone=True)
            time.sleep(1)
            form_keys_chick("en26", "ch", isone=True)
            time.sleep(1)
        print("第{}次执行结束等5S".format(i + 1))
        time.sleep(5)
    print("{}执行结束".format(sys._getframe().f_code.co_name))


def py26_en26_swich_oppo():
    for i in range(5):
        for j in range(10):
            form_keys_chick("py26", "ch", isone=True)
            time.sleep(1)
            form_keys_chick("en26", "ch", isone=True)
            time.sleep(1)
        print("第{}次执行结束等5S".format(i + 1))
        time.sleep(5)
    print("{}执行结束".format(sys._getframe().f_code.co_name))


def py26_emoji_swich_oppo():
    for i in range(5):
        for j in range(10):
            form_keys_chick("cand", "emojicand", isone=True)
            time.sleep(1)
            form_keys_chick("EmojiTab", "emojiback", isone=True)
            time.sleep(1)
        print("第{}次执行结束等5S".format(i + 1))
        time.sleep(5)
    print("{}执行结束".format(sys._getframe().f_code.co_name))


def py9_keyword_up_down_oppo():
    for i in range(5):
        for j in range(10):
            form_keys_chick("cand", "down", isone=True)
            time.sleep(1)
            form_keys_chick("cand", "down", isone=True)
            time.sleep(2)
        print("第{}次执行结束等5S".format(i + 1))
        time.sleep(5)
    print("{}执行结束".format(sys._getframe().f_code.co_name))


def yuyin():
    """
    拼音9下，反复使用语音输入"今天天气不错"2min，再收起键盘等待3min
    :return:
    """
    for i in range(20):
        from_keys_long_chick("py9", "space", 5000, isone=True)
        music()
        time.sleep(1)
        print("第{}次执行结束等5S".format(i + 1))
    form_keys_chick("cand", "down", isone=True)
    time.sleep(60 * 3)
    print("{}执行结束".format(sys._getframe().f_code.co_name))


def expression_package():
    """
    在微信中吊起输入法，点击工具栏笑脸进入表情包界面，发送20个表情包，再收起键盘等待3min(需要提前把无障碍模式，微信发送一次表情图，确认把切到表情面板默认为表情图)
    同时确认一下拼音9的空格是不是可以点击到微信的输入框（让微信起面板用，一般需要把空格的y坐标往下调一下）
    :return:
    """
    for i in range(20):
        form_keys_chick("cand", "emojicand", isone=True)
        time.sleep(3)
        if i % 2:
            form_keys_chick("EmojiTab", "emojiFirst", isone=True)
        else:
            form_keys_chick("EmojiTab", "end", isone=True)
        time.sleep(5)
        form_keys_chick("py9", "space", isone=True)
        time.sleep(1)
        print("第{}次执行结束等5S".format(i + 1))
    form_keys_chick("cand", "down", isone=True)
    time.sleep(60)
    print("1fenzhong")
    time.sleep(60)
    print("2fenzhong")
    time.sleep(60)
    print("{}执行结束".format(sys._getframe().f_code.co_name))


def back_free():
    """
    执行完以上场景，不再使用输入法，后台闲置15分钟
    :return:
    """
    for i in range(15):
        time.sleep(60)
        print("{}fenzhong".format(i + 1))
    print("{}执行结束".format(sys._getframe().f_code.co_name))


def reboot_test():
    """
    总清除手机，安装输入法设置为默认输入法，不插卡，不连wifi，也不启用其他应用，熄屏等待5分钟（第二次测试重启进行操作）
    :return:
    """
    iphone_reboot()
    for i in range(15):
        time.sleep(60)
        print("{}fenzhong".format(i + 1))
    print("{}执行结束".format(sys._getframe().f_code.co_name))


def long_press_num_candidate():
    """
    微信---数字面板长按后候选词---5
    :return:
    """
    pass


def long_press_py26_candidate():
    """
    微信---拼音26面板长按后候选词---e
    :return:
    """
    pass


def long_press_en26_candidate():
    """
    微信---英文26面板长按后候选词---a
    :return:
    """
    pass


def yuyin_input():
    """
    语音输入模式调整--反复使用语音输入
    :return:
    """
    pass


def hw_switch_model():
    """
    手写模式切换项
    :return:
    """
    pass


def music():
    wav_file = "voice.wav"
    pygame.mixer.init()
    pygame.mixer.music.load(wav_file)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    time.sleep(5)


if __name__ == "__main__":
    py9_case_oppo()
    # py26_case_oppo()
    # en26_case_oppo()
    # bh_case_oppo()
    # hw_case_oppo()
    # py9_en26_swich_oppo()
    # py26_en26_swich_oppo()
    # py26_emoji_swich_oppo()
    # py9_keyword_up_down_oppo()
    # yuyin()
    # expression_package()
    # back_free()
    # reboot_test()
