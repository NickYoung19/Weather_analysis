# 天气分析脚本
# 作者：Nick Peng
from Get_Weather import Query
from PIL import Image, ImageDraw, ImageFont
from pyecharts import Bar
from pyecharts import Geo
from pyecharts import Line
from pyecharts import Liquid
from pyecharts import Map
from pyecharts import Pie
from pyecharts import Radar
qr = Query()


# 天气预报图
def draw_weather_pic(city_name):
    data = qr.get_data(city_name)
    weather = data['weather']
    temperature = data['Ltemperature'] + '~' + data['Htemperature'] + '℃'
    img = Image.open('./mask.jpg')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('./fonts/simkai.ttf', size=50)
    draw.text((img.size[0]/6, img.size[1]/5), temperature, font=font, fill=(0, 177, 106))
    draw.text((img.size[0]/3, img.size[1]/5+150), weather, font=font, fill=(0, 128, 131))
    img.save('weather.jpg','jpeg')
    print('[INFO]:draw_weather_pic done...')


# 柱状图
def DrawBar(city_names):
    bar = Bar("城市气温柱状图")
    attrs1 = []
    attrs2 = []
    values1 = []
    values2 = []
    for cn in city_names:
        data = qr.get_data(cn)
        attrs1.append(cn)
        attrs2.append(cn)
        values1.append(data['Htemperature'])
        values2.append(data['Ltemperature'])
    bar.add("最高气温", attrs1, values1, mark_point=["average"])
    bar.add("最低气温", attrs2, values2, mark_point=["min", "max"])
    bar.render('weatherBar.html')


# 地理坐标系
def DrawGeo(city_names):
    data = []
    for cn in city_names:
        temp = qr.get_data(cn)
        data.append((cn, temp['pm25']))
    geo = Geo('全国部分城市空气质量', 'pm2.5',
              title_color='#fff',
              title_pos='center',
              width=1200,
              height=600,
              background_color='#404a59')
    attr, value = geo.cast(data)
    geo.add('', attr, value, visual_range=[0, 200], visual_text_color='#fff', symbol_size=15, is_visualmap=True, type='effectScatter')
    geo.render('weatherGeo.html')


# 折线图
def DrawLine(city_names):
    line = Line('城市气温折线图')
    attrs1 = []
    attrs2 = []
    values1 = []
    values2 = []
    for cn in city_names:
        data = qr.get_data(cn)
        attrs1.append(cn)
        attrs2.append(cn)
        values1.append(data['Htemperature'])
        values2.append(data['Ltemperature'])
    line.add("最高气温", attrs1, values1, is_smooth=True, mark_point=["average"])
    line.add("最低气温", attrs2, values2, is_smooth=True, mark_point=["average", "max"])
    line.render('weatherLine.html')


# 水球图
def DrawLiquid(city_name):
    data = int(qr.get_data(city_name)['SD'].strip('%')) / 100
    liquid = Liquid('%s城市湿度' % city_name)
    liquid.add('湿度', [data])
    liquid.render('weatherLiquid.html')


# 地图
def DrawMap(city_names):
    # 假设省会城市最高温度代表该省最高温度
    attrs = ['北京', '天津', '上海', '重庆',
             '河北', '山西', '辽宁', '吉林',
             '黑龙江', '江苏', '浙江', '安徽',
             '福建', '江西', '山东', '河南',
             '湖北', '湖南', '广东', '四川']
    values = []
    for cn in city_names:
        data = qr.get_data(cn)
        values.append(data['Htemperature'])
    map_ = Map('气温分布图', width=1200, height=600)
    map_.add('', attrs, values, maptype='china', is_visualmap=True, visual_text_color='#000')
    map_.render('weatherMap.html')


# 饼图
def DrawPie(city_names):
    attrs = []
    values = []
    for cn in city_names:
        attrs.append(cn)
        data = qr.get_data(cn)
        values.append(data['QY'])
    pie = Pie('部分城市相对气压饼图')
    pie.add('', attrs, values, is_label_show=True)
    pie.render('weatherPie.html')


# 雷达图
def DrawRadar(city_name):
    schema = [('最高气温', 45), ('气压', 1500), ('湿度', 100), ('最低气温', 45), ('PM2.5', 200)]
    data = qr.get_data(city_name)
    values = [[int(data['Htemperature']), int(data['QY']), int(data['SD'].strip('%')), int(data['Ltemperature']), int(data['pm25'])]]
    radar = Radar()
    radar.config(schema)
    radar.add('%s天气信息' % city_name, values, is_splitline=True, is_axisline_show=True)
    radar.render('weatherRadar.html')


if __name__ == '__main__':
    # city_names = ['上海', '北京', '南京', '杭州', '天津', '武汉']
    city_names = ['北京', '天津', '上海', '重庆',
                  '石家庄', '太原', '沈阳', '长春',
                  '哈尔滨', '南京', '杭州', '合肥',
                  '福州', '南昌', '济南', '郑州',
                  '武汉', '长沙', '广州', '成都']
    draw_weather_pic('郑州')
    DrawBar(city_names)
    DrawGeo(city_names)
    DrawLine(city_names)
    DrawLiquid('郑州')
    DrawMap(city_names)
    DrawPie(city_names)
    # DrawRadar('郑州')
