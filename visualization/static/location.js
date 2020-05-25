var myChartLocation = echarts.init(document.getElementById('location'),'shine');
var optionLocation = {
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            crossStyle: {
                color: '#999'
            }
        }
    },
    grid: {
        containLabel: true,
        x:20,
        y:50,
        x2:20,
        y2:10
    },
    toolbox: {
        feature: {
            dataView: {show: true, readOnly: false, title: 'dataView'},
            magicType: {show: true, type: ['line', 'bar'], title: {line: 'line', bar: 'bar', stack: 'stack', tiled: 'tiled'}},
            restore: {show: true, title: 'restore'},
            saveAsImage: {show: true, title: 'saveAsImage'}
        }
    },
    legend: {
        data: ['Tweet', 'Confirmed Cases']
    },
    xAxis: {
        type: 'category',
        data: ['NSW', 'VIC', 'QLD', 'WA', 'SA', 'ACT', 'TAS', 'NT'],
        axisPointer: {
            type: 'shadow'
        }
    },
    yAxis: [{
        type: 'value',
        name: 'Tweets'
    },
    {
        type: 'value',
        name: 'Cases',
        nameLocation: 'start'
    }],
    series: [
        {
            name: 'Tweet',
            data: [30477,33123,18053,9147,7445,5229,2285,500],
            type: 'bar'
        },
        {
            name: 'Confirmed Cases',
            type: 'line',
            yAxisIndex: 1,
            data: [3087,1603,1061,560,439,228,29,107]
        }
    ]
};

myChartLocation.setOption(optionLocation);