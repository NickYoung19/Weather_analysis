开发环境：

  Linux + Python版本：3.5

相关模块：

  PIL模块；requests模块；pyecharts模块；以及一些Python自带的模块。

补充说明：

  pyecharts模块安装时请依次执行以下命令：

  pip install echarts-countries-pypkg

  pip install echarts-china-provinces-pypkg

  pip install echarts-china-cities-pypkg

  pip install pyecharts

项目思路：

  利用国家气象局和百度天气查询API接口来获取当前天气数据，主要包括温度、湿度、气压等。

  获取相关数据之后利用pyecharts模块和PIL模块对数据进行可视化分析。

使用：

  在cmd窗口中运行 analysis.py 文件即可。
