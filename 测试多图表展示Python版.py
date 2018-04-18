'''
策略出处: https://www.botvs.com/strategy/84042
策略名称: 测试多图表展示Python版
策略作者: 小小梦
策略描述:



'''

import random
import time
def main():
    cfgA = {
        "title" : {"text" : "盘口图表"},
        "xAxis" : {
            "type" : "datetime"
        }, 
        "series" : [{
            "name" : "买一", 
            "data" : [],        
        },{
            "name" : "卖一",
            "data" : [],
        }]
    }

    cfgB = {
        "title" : {"text" : "差价图"},
        "xAxis" : {
            "type" : "datetime"
        },
        "series" : [{
            "name" : "差价",
            "type" : "column",
            "data" : [],
        }]
    }

    cfgC = {
        "__isStock" : False,
        "title" : {
            "text" : "饼图"
        },
        "series" : [{
            "type" : "pie",
            "name" : "one",
            "data" : [
                ["A", 25],
                ["B", 25],
                ["C", 25],
                ["D", 25],
            ]
        }]
    }

    chart = Chart([cfgA, cfgB, cfgC])
    chart.reset()
    chart.add(3, {
        "name" : "ZZ", 
        "y" : random.random() * 100
    })


    chart.update([cfgA, cfgB, cfgC])
    chart.add(0, [_N(time.time() * 1000, 0), 50])
    chart.add(1, [_N(time.time() * 1000, 0), 80])
    chart.add(2, [_N(time.time() * 1000, 0), 90])
    chart.add(3, {
        "name" : "ZZ",
        "y" : random.random() * 100
    }, -1)

