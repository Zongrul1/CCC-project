var myChartHashtag = echarts.init(document.getElementById('hashtag'),'shine');
var optionHashtag = {
dataset: {
source: [
    ['score', 'amount', 'product'],
    [721, 721, '#kawasaki'],
    [748, 748, '#pandemic'],
    [888, 888, '#children'],
    [972, 972, '#australia'],
    [1202, 1202, '#herdimmunity'],
    [1472, 1472, '#9news'],
    [1788, 1788, '#china'],
    [1793, 1793, '#7news'],
    [2936, 2936, '#breaking'],
    [5380, 5380, '#auspol']       
]
},
toolbox: {
    feature: {
        saveAsImage: {show: true, title: 'saveAsImage'}
    }
},
grid: {
    containLabel: true,
    x:0,
    y:30,
    x2:20,
    y2:5
},
xAxis: {name: ''},
yAxis: {name: '',type: 'category'},
visualMap: {
orient: 'horizontal',
show: false,
left: 'center',
min: 700,
max: 6000,
text: ['High Score', 'Low Score'],
dimension: 0,
inRange: {
    color: ['#E74C3C', '#B03A2E']
}
},
series: [
{
    type: 'bar',
    label: {
        show: true
    },
    encode: {
        x: 'occurrence',
        y: 'product'
    }
}
]
};

myChartHashtag.setOption(optionHashtag);