---
title: "Hide Data Series on Google Chart by Clicking Legend"
site: stackoverflow
question_id: 73849443
answer_id: 73855322
url: https://stackoverflow.com/a/73855322
author: "WhiteHat"
author_url: https://stackoverflow.com/users/5090771
posted: 2022-09-26T14:02:52Z
last_edited: never
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 87624507a2a5106f01b25f22710e1fc87eb8331ae6ad992c7b4c1ffa561bfa75
role: another answer on the same question, kept as context; not my work
---

# Answer by [WhiteHat](https://stackoverflow.com/users/5090771) — 2022-09-26

Posted on Stack Overflow, <https://stackoverflow.com/a/73855322>, 2022-09-26; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

the issue is with the dashboard.  
when the slider is used, the dashboard re-draws the chart with the original data view,  
which includes the column values for all series.  
but the chart keeps the previous options, which is why the series is greyed out.  

you will need lose the dashboard and draw the chart and slider independently.  

which also means you will need to manually filter the data based on the state of the slider.  

but doing so raises a few issues.

you will need to maintain the chart selection outside of the function to handle the series toggle.  

and you will need to use a data table instead of a data view as the main source of data.  
otherwise, you will lose the original rows when you filter the data view.  

following is what I came up with to keep everything in sync.  

    google.charts.load('current', {packages: ['controls']}).then(initialize);

    function initialize() {
      var query = new google.visualization.Query('https://docs.google.com/spreadsheets/d/1001YnF8LCwKyzpS4pgmZnwFVigL-LlnqwWn6xjnso2k/edit#gid=0&range=A:BT');
          query.send(drawDashboard);
    }

    function drawDashboard(response) {

        var data = response.getDataTable();
        //Asign units of 'mm' to data.
        var formatMS = new google.visualization.NumberFormat({pattern: '# mm'});

        // format data into mm.
        for (var colIndex = 1; colIndex < data.getNumberOfColumns(); colIndex++) {formatMS.format(data, colIndex);}
        var dataView = new google.visualization.DataView(data);
        dataView.setColumns([0,1,2,{sourceColumn: 3, role: 'interval'}, {sourceColumn: 4, role: 'interval'}, 5,{sourceColumn: 6, 'type': 'string', role: 'tooltip', 'p': {'html': true}},7,8,9,10,11,12,13,14,15,{sourceColumn: 16, role: 'interval'}, {sourceColumn: 17, role: 'interval'}, 18,{sourceColumn: 19, 'type': 'string', role: 'tooltip', 'p': {'html': true}},20,21,22,23,24,25,26,27,28,{sourceColumn: 29, role: 'interval'}, {sourceColumn: 30, role: 'interval'},31,{sourceColumn: 32, 'type': 'string', role: 'tooltip', 'p': {'html': true}},33,34,35,36,37,38,39,40,41,{sourceColumn: 42, role: 'interval'}, {sourceColumn: 43, role: 'interval'}, 44,{sourceColumn: 45, 'type': 'string', role: 'tooltip', 'p': {'html': true}},46,47,48,49,50,51,52,53,54,{sourceColumn: 55, role: 'interval'}, {sourceColumn: 56, role: 'interval'}, 57,{sourceColumn: 58, 'type': 'string', role: 'tooltip', 'p': {'html': true}},59,60,61,62,63,64,65,66,67,68,69,70,71]);
        var viewColumns = [0,7,20,33,46,59,66,67,68,69,70,71];

        // use data table as main source of data
        dataView = dataView.toDataTable();

        var YearPicker = new google.visualization.ControlWrapper({
          controlType: 'NumberRangeFilter',
          containerId: 'filter_div',
          dataTable: dataView,  // <-- add data table here in order to draw independently
          options: {
            maxValue: 2150,
            minValue: 1891,
            filterColumnLabel: 'Year',
            ui: {
              cssClass: 'filter-date',
              format: {pattern: '0000'},
              labelStacking: 'vertical',
              allowTyping: true,
              allowMultiple: false
            }
          },
          state: {lowValue: 1891, highValue: 2150},
        });

        var series = {
          0: {color:'navy', visibleInLegend: true}, //Auckland
          1: {color:'green', visibleInLegend: true }, //Taranaki
          2: {color:'gold', visibleInLegend: true}, //Wellington
          3: {color:'red', visibleInLegend: true}, //Lyttelton
          4: {color:'DeepSkyBlue', visibleInLegend: true}, //Dunedin
          5: {color:'#47d045', visibleInLegend: true}, //NZ RCP2.6 M
          6: {color:'#0e038d', visibleInLegend: true}, //NZ RCP4.5 M
          7: {color:'#b8bb62', visibleInLegend: true}, //NZ RCP8.5 M
          8: {color:'#b22123', visibleInLegend: true}, //NZ RCP8.5 H
          9: {color:'blue', visibleInLegend: true}, //NZ Mean
          10: {color:'blue', visibleInLegend: false}, //NZ Mean
        };

        // save series colors
        var seriesColors = {};
        for (var column in series) {
          if (series.hasOwnProperty(column)) {
            seriesColors[column] = series[column].color;
          }
        }

        var MSLChart = new google.visualization.ChartWrapper({
          chartType: 'LineChart',
          containerId: 'chart_div',
          dataTable: dataView,
          options: {
            fontSize: '20',
            title: 'NZ Annual Relative Mean Sea Level Summary',
            hAxis: {title: 'Year', format: '0000'},
            vAxis: {title: 'Height above 1986-2005 IPCC Baseline (mm)', format:'###0'},
            height: 600,
            chartArea: {height: '81%', width: '85%', left: 100},
            legend: {position: 'top', maxLines: 5, alignment: 'start', textStyle: {fontSize: 9}},
            colors: ['blue'],
            tooltip: {
              isHtml: true
            },
            trendlines: {
              9: {
                type: 'linear',
                color: 'black',
                visibleInLegend: true,
                showR2: true,
              },
              10: {
                type: 'polynomial',
                color: 'purple',
                degree: 2,
                visibleInLegend: true,
                showR2: true,
              },
            },
            series: series,
            intervals: { 'style':'bars','color': '#6292dc' },
            interpolateNulls: 'True',
          },
          view: {columns: viewColumns}
        });

        // save selection outside of toggle series function
        var sel;

        var columns = [];
        for (var i = 0; i < dataView.getNumberOfColumns(); i++) {
          columns.push(i);
        }

        // use named function for statechange to also be called from select event
        google.visualization.events.addListener(YearPicker, 'statechange', onState);

        // select event
        google.visualization.events.addListener(MSLChart, 'select', function () {
          // save selection
          sel = MSLChart.getChart().getSelection();

          // call state change to display correct rows
          onState(true);  // <-- true argument to trigger series toggle
        });

        // handle state change on slider
        function onState(toggleColumns) {
          var state = YearPicker.getState();
          state.lowValue = Math.min(2021, state.lowValue);
          YearPicker.setState({
            lowValue: state.lowValue,
            highValue: state.highValue
          });
          YearPicker.draw();

          var view = new google.visualization.DataView(dataView);
          var rows = dataView.getFilteredRows([{
            column: 0,
            minValue: state.lowValue,
            maxValue: state.highValue
          }]);
          view.setRows(rows);
          redrawChart(view, (toggleColumns === true));  // <-- we only want to toggle series if called from select event
        }

        // toggle series
        function redrawChart(view, toggleColumns) {
          var chartArea = MSLChart.getChart().getChartLayoutInterface().getChartAreaBoundingBox();
          var vAxisTop = MSLChart.getChart().getChartLayoutInterface().getVAxisValue(chartArea.top);
          var vAxisBtm = MSLChart.getChart().getChartLayoutInterface().getVAxisValue(chartArea.top + chartArea.height);

          // toggle columns?
          if (toggleColumns) {
            // if selection length is 0, we deselected an element
            if (sel.length > 0) {
               // if row is undefined, we clicked on the legend
               if ((sel[0].row === null) && (sel[0].column > 0)) {
                   // get actual column number from view
                   var col = viewColumns[sel[0].column];
                   if (columns[col] == col) {
                      // hide the data series
                      columns[col] = {
                         label: dataView.getColumnLabel(col),
                         type: dataView.getColumnType(col),
                         calc: function () {
                            return null;
                         }
                      };

                      // grey out the legend entry
                      series[sel[0].column - 1].color = '#CCCCCC';
                  } else {
                      // show the data series
                      columns[col] = col;
                      series[sel[0].column - 1].color = seriesColors[sel[0].column - 1];
                  }

               }
            }
          }

          // set new view columns
          view.setColumns(columns);
          MSLChart.setDataTable(view);

          // prevent y-axis from changing when series is removed
          MSLChart.setOption('series', series);
          MSLChart.setOption('vAxis.viewWindow.max', vAxisTop);
          MSLChart.setOption('vAxis.viewWindow.min', vAxisBtm);

          // re-draw chart
          MSLChart.draw();
        }

        // draw slider and chart initially
        YearPicker.draw();
        MSLChart.draw();
    }

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Bryan Ward](https://stackoverflow.com/users/11575522)** (2022-09-27): Thanks @WhiteHat.  I've been tearing my hair our with this since you answered the original question above.  Would never have come up with the above solution in a million years.  Much appreciated.
