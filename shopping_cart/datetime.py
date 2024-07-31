from datetime import datetime


def gLeapYear(y):
    if (y % 4 == 0) and ((y % 100 != 0) or (y % 400 == 0)):
        return True
    else:
        return False


def sLeapYear(y):
    ary = [1, 5, 9, 13, 17, 22, 26, 30]
    result = False
    b = y % 33
    if b in ary:
        result = True
    return result


def shamsiDate(gyear, gmonth, gday):
    _gl = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    _g = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    deydiffjan = 10
    if gLeapYear(gyear - 1):
        deydiffjan = 11
    if gLeapYear(gyear):
        gd = _gl[gmonth - 1] + gday
    else:
        gd = _g[gmonth - 1] + gday

    if gd > 79:
        sy = gyear - 621
        gd = gd - 79
        if gd <= 186:
            gmod = gd % 31
            if gmod == 0:
                sd = 31
                sm = int(gd / 31)
            else:
                sd = gmod
                sm = int(gd / 31) + 1
        else:
            gd = gd - 186
            gmod = gd % 30
            if gmod == 0:
                sd = 30
                sm = int(gd / 30) + 6
            else:
                sd = gmod
                sm = int(gd / 30) + 7
    else:
        sy = gyear - 622
        gd = gd + deydiffjan
        gmod = gd % 30
        if gmod == 0:
            sd = 30
            sm = int(gd / 30) + 9
        else:
            sd = gmod;
            sm = int(gd / 30) + 10

    result = [sy, sm, sd]
    return result


class timedatePersian():
    tarikh = datetime.now()
    x_years = tarikh.year
    x_month = tarikh.month
    x_day = tarikh.day

    persian_month = ''
    y = shamsiDate(x_years, x_month, x_day)

    if y[1] == 1:
        persian_month = 'فروردین'
    elif y[1] == 2:
        persian_month = 'اردیبهشت'
    elif y[1] == 3:
        persian_month = 'خرداد'
    elif y[1] == 4:
        persian_month = 'تیر'
    elif y[1] == 5:
        persian_month = 'مرداد'
    elif y[1] == 6:
        persian_month = 'شهریور'
    elif y[1] == 7:
        persian_month = 'مهر'
    elif y[1] == 8:
        persian_month = 'آبان'
    elif y[1] == 9:
        persian_month = 'آذر'
    elif y[1] == 10:
        persian_month = 'دی'
    elif y[1] == 11:
        persian_month = 'بهمن'
    elif y[1] == 12:
        persian_month = 'اسفند'

    today_date = f"{y[2]} {persian_month} ماه {y[0]}"
