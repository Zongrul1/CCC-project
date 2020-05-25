var myChartLang = echarts.init(document.getElementById('lang'),'shine');
var optionLang = {
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)'
    },
    toolbox: {
        show: true,
        feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            magicType: {
                show: true,
                type: ['pie', 'funnel']
            },
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    grid: {
        containLabel: true,
        x:0,
        y:5,
        x2:20,
        y2:5
    },
    series: [
        {
            name: 'Top 10 Languages',
            type: 'pie',
            radius: [45, 70],
            data: [
                {value: 24918, name: 'Spanish'},
                {value: 5798, name: 'French'},
                {value: 3668, name: 'Portuguese'},
                {value: 2949, name: 'Japanese'},
                {value: 2758, name: 'Indonesian'},
                {value: 2676, name: 'Hindi'},
                {value: 2660, name: 'Italian'},
                {value: 2046, name: 'Catalan'},
                {value: 1163, name: 'German'},
                {value: 1056, name: 'Thai'}
            ]
        }
    ]
};

myChartLang.setOption(optionLang);