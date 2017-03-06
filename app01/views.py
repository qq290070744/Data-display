from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
import time, json, pymysql, collections
from app01.models import *
from django.http import JsonResponse
# Create your views here.
date = time.strftime('%Y-%m-%d')

yue = time.localtime(float(time.time()) - 86400)
timeStr = time.strftime("%Y%m%d", yue)
yue = time.strftime('%Y-%m-01', yue)

# mysql连接#
from untitled1 import settings

host = settings.DATABASES['default']['HOST']  # '121.201.68.21'
port = settings.DATABASES['default']['PORT']  # 3307
user = settings.DATABASES['default']['USER']  # 'jiang'
passwd = settings.DATABASES['default']['PASSWORD']  # ''
db = settings.DATABASES['default']['NAME']  # 'daxiangzhanshi'


def acc_login(request):
    if request.method == "POST":
        print(request.POST)
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            login(request, user)
            return redirect('/')
        else:
            error = "error"
            return render(request, "login.html", {"login_error": error})

    return render(request, "login.html")


@login_required
def acc_logout(requrst):
    logout(requrst)
    return redirect("/")


@login_required
def ip(request):
    date = time.strftime('%Y-%m-%d')
    # data = The_number_of_clicks.objects.filter(updatetime__gte=yue).order_by('-number')
    data = The_number_of_clicks.objects.filter(updatetime__gte=yue).values('province_name').annotate(
        number=Sum('number')).values('province_name', 'number').order_by('-number')

    data1 = []
    data2 = []
    data3 = []
    num = 1
    qita = 0
    total = 0

    for i in data:

        total += float(i['number'])
        data2.append(i['province_name'])
        data1.append(i['number'])
        if num <= 12:
            data3.append({"name": i['province_name'], "y": i['number']})
        else:
            qita += float(i['number'])

        num += 1
    data3.append({"name": "其他", "y": qita})

    # ipdata = source_ip.objects.filter(updatetime__gte=yue).order_by('-number')
    ipdata = source_ip.objects.filter(updatetime__gte=yue).values('province_name').annotate(
        number=Sum('number')).values('province_name', 'number').order_by('-number')
    ipdata1 = []
    ipdata2 = []
    ipdata3 = []
    ipnum = 1
    ipqita = 0
    iptotal = 0
    ipdaic = {}
    for ip in ipdata:
        ipdaic[ip['province_name']] = ip['number']
        iptotal += float(ip['number'])
        ipdata2.append(ip['province_name'])
        ipdata1.append(ip['number'])
        if ipnum <= 10:
            ipdata3.append({"name": ip['province_name'], "y": ip['number']})
        else:
            ipqita += float(ip['number'])

        ipnum += 1
    ipdata3.append({"name": "其他", "y": ipqita})
    print("用户正在访问点击次数和来源ip各省统计图", yue)
    return render(request, 'ip.html',
                  {"data": json.dumps(data2), "data1": json.dumps(data1), "data3": json.dumps(data3),
                   "total_clicks": total, "ipdata": json.dumps(ipdata2), "ipdata1": json.dumps(ipdata1),
                   "ipdata3": json.dumps(ipdata3), "iptotal_clicks": iptotal, "yue": yue.replace("-", "")[0:6]})


@login_required
def Business_daily_traffics(request):
    date = time.strftime('%Y-%m-%d')
    shgdata = Business_daily_traffic.objects.filter(Business_name='生活馆').order_by('-date')[:10]
    shgdate = []
    shgtraffic = []
    for i in shgdata:
        # print(i.date,i.traffic)
        shgdate.append(i.date)
        shgtraffic.append(i.traffic)

    dsdata = Business_daily_traffic.objects.filter(Business_name='电商').order_by('-date')[:10]
    dsdate = []
    dstraffic = []
    for i in dsdata:
        # print(i.date,i.traffic)
        dsdate.append(i.date)
        dstraffic.append(i.traffic)

    ssodata = Business_daily_traffic.objects.filter(Business_name='SSO').order_by('-date')[:10]
    ssodate = []
    ssotraffic = []
    for i in ssodata:
        # print(i.date,i.traffic)
        ssodate.append(i.date)
        ssotraffic.append(i.traffic)

    netdata = Business_daily_traffic.objects.filter(Business_name='.NET').order_by('-date')[:10]
    netdate = []
    nettraffic = []
    for i in netdata:
        # print(i.date,i.traffic)
        netdate.append(i.date)
        nettraffic.append(i.traffic)

    print("用户正在访问Business_daily_traffics各业务每天访问量")
    return render(request, 'business_daily_traffic.html',
                  {"shgdate": json.dumps(shgdate), "shgtraffic": json.dumps(shgtraffic), \
                   "dsdate": json.dumps(dsdate),
                   "dstraffic": json.dumps(dstraffic),
                   "ssodate": json.dumps(ssodate),
                   "ssotraffic": json.dumps(ssotraffic),
                   "netdate": json.dumps(netdate),
                   "nettraffic": json.dumps(nettraffic),
                   })


@login_required
def Heat_chart(request):
    date = time.strftime('%Y-%m-%d')
    ipdata = provinces_rmb.objects.filter(updatetime__gte=date)
    ipdict = {}
    for i in ipdata:
        ipdict[i.name] = i.rmb
    print("用户正在访问Heat_chart")
    return render(request, 'Heat_chart.html', {"ipdict": json.dumps(ipdict), "Heat_chart": ipdata})


@login_required
def index(request):
    print("用户正在访问主页")
    return render(request, 'index.html')


@login_required
def real_time(reauest):
    date = time.strftime('%Y-%m-%d')
    data = real.objects.filter(updatetime__gte=date).order_by('time')
    time_list = []
    rmb_list = []
    num_list = []
    for i in data:
        # print(i.time)
        time_list.append(i.time)
        rmb_list.append(i.rmb)
        num_list.append(i.numner)
        print("用户正在访问real_time")
    return render(reauest, 'real_time.html', {"time_list": json.dumps(time_list), "rmb_list": json.dumps(rmb_list),
                                              "num_list": json.dumps(num_list)})


@login_required
def Big_picture(request):  # 总的
    date = time.strftime('%Y-%m-%d')
    ipdata = provinces_rmb.objects.filter(updatetime__gte=date).order_by('-rmb')
    ipdict = {}
    province_rmb_list = []
    province__list = []
    num = 0
    qitarmb = 0
    for i in ipdata:
        ipdict[i.name] = i.rmb
        province__list.append(i.name)
        if num <= 9:
            province_rmb_list.append({'value': i.rmb, 'name': i.name})
        else:
            qitarmb += float(i.rmb)
        num += 1
    province_rmb_list.append({'value': qitarmb, 'name': "其他"})
    #

    realdata = real.objects.filter(updatetime__gte=date).order_by('time')
    time_list = []
    rmb_list = []
    num_list = []
    for i in realdata:
        # print(i.time)
        time_list.append(i.time)
        rmb_list.append(i.rmb)
        num_list.append(i.numner)

    data = The_number_of_clicks.objects.filter(updatetime__gte=date).order_by('-number')
    data1 = []
    data2 = []
    data3 = []
    num = 1
    qita = 0
    total = 0
    for i in data:
        total += float(i.number)
        data2.append(i.province_name)
        data1.append(i.number)
        if num <= 12:
            data3.append({"name": i.province_name, "y": i.number})
        else:
            qita += float(i.number)

        num += 1
    data3.append({"name": "其他", "y": qita})

    ipdata_ = source_ip.objects.filter(updatetime__gte=date).order_by('-number')
    ipdata1 = []
    ipdata2 = []
    ipdata3 = []
    ipnum = 1
    ipqita = 0
    iptotal = 0
    ipdaic = {}
    province_list = []
    for ip in ipdata_:
        ipdaic[ip.province_name] = ip.number
        iptotal += float(ip.number)
        ipdata2.append(ip.province_name)
        ipdata1.append(ip.number)
        if ipnum <= 10:
            ipdata3.append({"name": ip.province_name, "value": ip.number})
        else:
            ipqita += float(ip.number)

        ipnum += 1
        province_list.append(ip.province_name)
    ipdata3.append({"name": "其他", "value": ipqita})

    goods_set = set()
    goods_and_rmb = []
    goods = subclass.objects.all().order_by('categoriesId')
    for i in goods:
        goods_set.add(i.categoriesName)
        goods_set.add(i.name)

        goods_and_rmb.append({"value": i.total_rmb, "name": i.name})

    good_list = list(goods_set)

    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                           charset='UTF8')
    cur = conn.cursor()
    sql = "select sum(total_rmb),categoriesName  from app01_subclass group by categoriesName order by categoriesId"
    cur.execute(sql)
    cur.close()
    conn.close()
    commodity_categories = []
    for i in cur:
        # print(i)
        commodity_categories.append({"value": i[0], "name": i[1]})

    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                           charset='UTF8')
    cur = conn.cursor()
    sql = "select sum(total_rmb),categoriesName  from app01_subclass group by categoriesName order by sum(total_rmb) desc "
    cur.execute(sql)
    cur.close()
    conn.close()
    charts = {}
    All = 0
    for i in cur:
        # print(i)
        # commodity_categories.append({"value": i[0], "name": i[1]})
        charts[i[1]] = i[0]
        All += float(i[0])
    components = {}
    goods = subclass.objects.all()
    for i in goods:
        components[i.name] = i.total_rmb
    charts = collections.OrderedDict(sorted(charts.items(), key=lambda t: t[1]))  # 对字典进行排序
    components = collections.OrderedDict(sorted(components.items(), key=lambda t: t[1]))

    print("用户正在访问总的")
    return render(request, 'Big_picture.html',
                  {"ipdict": json.dumps(ipdict), "time_list": json.dumps(time_list), "rmb_list": json.dumps(rmb_list),
                   "num_list": json.dumps(num_list), "data": json.dumps(data2), "data1": json.dumps(data1),
                   "data3": json.dumps(data3), "total_clicks": total, "ipdata": json.dumps(ipdata2),
                   "ipdata1": json.dumps(ipdata1), "ipdata3": json.dumps(ipdata3), "iptotal_clicks": iptotal,
                   "goods_list": json.dumps(good_list), "goods_and_rmb": json.dumps(goods_and_rmb),
                   "commodity_categories": json.dumps(commodity_categories),
                   "province_list": json.dumps(province_list), "province_rmb_list": json.dumps(province_rmb_list),
                   "province__list": json.dumps(province__list), "charts": json.dumps(charts), "all": All,
                   "components": json.dumps(components), "Heat_chart": ipdata})


@login_required
def first_10(request):
    date = time.strftime('%Y-%m-%d')
    goods_set = set()
    goods_and_rmb = []

    goods = subclass.objects.all().order_by('categoriesId')
    for i in goods:
        goods_set.add(i.name)
        goods_set.add(i.categoriesName)

        goods_and_rmb.append({"value": i.total_rmb, "name": i.name})

    good_list = list(goods_set)

    data = subclass.objects.all().values('categoriesName').annotate(total_rmb=Sum('total_rmb')).values('categoriesName',
                                                                                                       'total_rmb').order_by(
        'categoriesId')

    commodity_categories = []
    for i in data:
        # print(i)
        commodity_categories.append({"value": i['total_rmb'], "name": i['categoriesName']})

    print("用户正在访问first_10")
    return render(request, '10大.html', {"goods_list": json.dumps(good_list), "goods_and_rmb": json.dumps(goods_and_rmb),
                                        "commodity_categories": json.dumps(commodity_categories)})


@login_required
def City_trading_volumes(request):
    date = time.strftime('%Y-%m-%d')
    City_data = City_trading_volume.objects.filter(updatetime__gte=date)
    City_data_list = []
    for i in City_data:
        # print(i.city_name,i.city_rmb)
        City_data_list.append({'name': i.city_name, 'value': i.city_rmb})
    return render(request, 'City_trading_volume1.html',
                  {"City_data_list": json.dumps(City_data_list), "City_data": City_data})


def total_rmb(request):
    date = time.strftime('%Y-%m-%d')
    data = real.objects.filter(updatetime__gte=date)
    total = 0
    for i in data:
        total += float(i.rmb)

    return HttpResponse('({"n":%s})' % int(total))


@login_required
def first10_1(request):
    date = time.strftime('%Y-%m-%d')
    data = subclass.objects.all().values('categoriesName').annotate(total_rmb=Sum('total_rmb')).values('categoriesName',
                                                                                                       'total_rmb').order_by(
        '-total_rmb')

    charts = {}
    All = 0
    for i in data:
        # print(i)
        # commodity_categories.append({"value": i[0], "name": i[1]})
        charts[i['categoriesName']] = i['total_rmb']
        All += float(i['total_rmb'])
    components = {}
    goods = subclass.objects.all()
    for i in goods:
        components[i.name] = i.total_rmb

    charts = collections.OrderedDict(sorted(charts.items(), key=lambda t: t[1]))
    components = collections.OrderedDict(sorted(components.items(), key=lambda t: t[1]))
    return render(request, '10大商品矩形和饼图.html',
                  {"charts": json.dumps(charts), "all": All, "components": json.dumps(components)})


@login_required
def business_real_time_accesss(request):  # 各个业务间隔5分钟实时访问量
    date = time.strftime('%Y-%m-%d')
    business_real_time_access_data = business_real_time_access.objects.filter(updatetime__gte=date).order_by('time')
    time_list = []
    SSO_li = []
    shg_li = []
    NET_li = []
    ds_li = []
    for i in business_real_time_access_data:
        # print(i.business_name,i.access_count,i.time)

        if i.business_name == 'SSO':
            SSO_li.append(i.access_count)
        if i.business_name == "生活馆":
            shg_li.append(i.access_count)
        if i.business_name == ".NET":
            NET_li.append(i.access_count)
        if i.business_name == "电商":
            ds_li.append(i.access_count)
            time_list.append(i.time)

    # print(time_list)
    return render(request, 'business_real_time_access.html',
                  {"time_list": json.dumps(time_list), "SSO_li": json.dumps(SSO_li), "shg_li": json.dumps(shg_li),
                   "NET_li": json.dumps(NET_li), "ds_li": json.dumps(ds_li)})


@login_required
def pie_custom(request):
    date = time.strftime('%Y-%m-%d')
    data = subclass.objects.all().values('categoriesName').annotate(total_rmb=Sum('total_rmb')).values('categoriesName',
                                                                                                       'total_rmb').order_by(
        '-total_rmb')

    charts = []
    All = 0
    for i in data:
        charts.append({'value': i['total_rmb'], 'name': i['categoriesName']})
        All += float(i['total_rmb'])

    return render(request, 'pie-custom.html',
                  {"charts": json.dumps(charts), "All": All})


def tables(request):
    date = time.strftime('%Y-%m-%d')
    data = subclass.objects.all().values('categoriesName').annotate(total_rmb=Sum('total_rmb')).values('categoriesName',
                                                                                                       'total_rmb').order_by(
        '-total_rmb')

    charts = {}
    All = 0
    for i in data:
        # print(i)
        # commodity_categories.append({"value": i[0], "name": i[1]})
        charts[i['categoriesName']] = i['total_rmb']
        All += float(i['total_rmb'])
    components = {}
    goods = subclass.objects.all()[:10]
    for i in goods:
        components[i.name] = round((float(i.total_rmb) / All) * 100, 2)

    charts = collections.OrderedDict(sorted(charts.items(), key=lambda t: t[1]))
    components = collections.OrderedDict(sorted(components.items(), key=lambda t: t[1]))

    return render(request, 'table.html',
                  {"charts": json.dumps(charts), "all": All, "components": components.items()})

#############ajax##########
def add(request):
    if request.GET:
        a = request.GET['a']
        b = request.GET['b']
        jieguo = float(a) + float(b)
        print(jieguo)
        return HttpResponse(jieguo)

    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    #return JsonResponse(name_dict)
    return render(request, 'ajax.html')

def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)

def real_time_time_list(reauest):
    date = time.strftime('%Y-%m-%d')
    data = real.objects.filter(updatetime__gte=date).order_by('time')
    time_list = []
    rmb_list = []
    num_list = []
    for i in data:
        # print(i.time)
        time_list.append(i.time)
        rmb_list.append(i.rmb)
        num_list.append(i.numner)
        print("ajax正在访问 real_time_time_list")

    #return render(reauest, 'real_time.html', {"time_list": json.dumps(time_list), "rmb_list": json.dumps(rmb_list),"num_list": json.dumps(num_list)})
    trn_list=[time_list,rmb_list,num_list]
    return JsonResponse(trn_list,safe=False)


def business_real_time_accesss_ajax(request):
    date = time.strftime('%Y-%m-%d')
    business_real_time_access_data = business_real_time_access.objects.filter(updatetime__gte=date).order_by('time')
    time_list = []
    SSO_li = []
    shg_li = []
    NET_li = []
    ds_li = []
    for i in business_real_time_access_data:
        # print(i.business_name,i.access_count,i.time)

        if i.business_name == 'SSO':
            SSO_li.append(i.access_count)
        if i.business_name == "生活馆":
            shg_li.append(i.access_count)
        if i.business_name == ".NET":
            NET_li.append(i.access_count)
        if i.business_name == "电商":
            ds_li.append(i.access_count)
            time_list.append(i.time)


    tssnd=[time_list,NET_li,SSO_li,ds_li,shg_li]
    return JsonResponse(tssnd,safe=False)
    #return render(request, 'business_real_time_access.html',{"time_list": json.dumps(time_list), "SSO_li": json.dumps(SSO_li), "shg_li": json.dumps(shg_li),"NET_li": json.dumps(NET_li), "ds_li": json.dumps(ds_li)})

def Heat_chart_ajax(request):
    date = time.strftime('%Y-%m-%d')
    ipdata = provinces_rmb.objects.filter(updatetime__gte=date)
    ipdict = {}
    for i in ipdata:
        ipdict[i.name] = i.rmb
    print("用户正在访问Heat_chart_ajax")
    return JsonResponse(ipdict,safe=False)