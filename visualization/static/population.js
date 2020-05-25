var myChartPopulation = echarts.init(document.getElementById('population'),'shine');
var optionPopulation = {
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        },
        formatter: function (params) {
            var tar = params[1];
            return tar.name + '<br/>' + tar.seriesName + ' : ' + tar.value;
        }
    },
    grid: {
        containLabel: true,
        x:0,
        y:5,
        x2:20,
        y2:5
    },
    yAxis: {
        type: 'category',
        splitLine: {show: false},
        data: ['NSW', 'VIC', 'QLD', 'WA', 'SA', 'TAS', 'NT', 'ACT']
    },
    xAxis: {
        type: 'value'
    },
    series: [
        {
            name: 'help',
            type: 'bar',
            stack: 'all',
            itemStyle: {
                barBorderColor: 'rgba(0,0,0,0)',
                color: 'rgba(0,0,0,0)'
            },
            emphasis: {
                itemStyle: {
                    barBorderColor: 'rgba(0,0,0,0)',
                    color: 'rgba(0,0,0,0)'
                }
            },
            label: {
                show: true,
                position: 'insideLeft'
            },
            data: [16731233, 10409585, 5480433, 2904981, 1181310, 659158, 411667, 0]
        },
        {
            name: 'Population',
            type: 'bar',
            stack: 'all',
            label: {
                show: true,
                position: 'inside'
            },
            label: {
                show: true,
                position: 'insideLeft'
            },
            data: [7861674, 6321648, 4929152, 2575452, 1723671, 522152, 247491, 411667]
        }
    ]
};

myChartPopulation.setOption(optionPopulation);