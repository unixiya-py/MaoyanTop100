import random

useragent = '''Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1
Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1
Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)
Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50
Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50
Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)
Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)'''


def get_useragent():
    useragent_list = useragent.split('\n')
    length = len(useragent_list)
    return useragent_list[random.randint(0, length - 1)]


if __name__ == '__main__':
    print(get_useragent())
