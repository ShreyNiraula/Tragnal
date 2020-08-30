  // line graph (day data)
  new Chart(document.getElementById("myLineGraph"), {
      type: 'line',
      data: {
        labels: {{ labels_days }},
        datasets : [{
                  label: "Average Traffic Volume",
                  data : {{ datas_days }},
                  fill: false,
                  lineTension: 0.1,
                  backgroundColor: "rgba(127,192,192,0.4)",
                  borderColor: "#fff",
                  borderCapStyle: 'butt',
                  borderDash: [],
                  borderDashOffset: 0.0,
                  borderJoinStyle: 'miter',
                  pointBorderColor: "rgba(75,192,192,1)",
                  pointBackgroundColor: "#fff",
                  pointBorderWidth: 1,
                  pointHoverRadius: 5,
                  pointHoverBackgroundColor: "rgba(75,192,192,1)",
                  pointHoverBorderColor: "rgba(220,220,220,1)",
                  pointHoverBorderWidth: 2,
                  pointRadius: 1,
                  pointHitRadius: 10,
                  spanGaps: false
              }]
      },
      options: {
                  legend: {
                            display: true,
                            labels: {
                                fontColor: 'rgb(255, 99, 132)',
                                fontSize : 18,
                            }
                        },
                    scales: {
                        yAxes: [{
                            scaleLabel :{
                                display: true,
                                labelString: 'Number of vehicle / hour',
                                fontSize : 15,
                                fontColor : "#cf3408",
                            },
                            ticks: {
                                beginAtZero: true,
                                fontColor: "#ffa500"
                            }
                        }],
                        xAxes: [{
                            //gridLines: {
                            //	display: true,
                            //	color : "#606060",
                            //},
                            scaleLabel :{
                                display: true,
                                labelString: 'Time (AM to PM)',
                                fontSize : 15,
                                fontColor : "#cf3408",
                            },
                            ticks: {
                                fontColor: "#ffa500",
                            }
                        }],
                    },
                },
      });

  // bargraph (week data)
  new Chart(document.getElementById("myBarGraph"), {
      type: 'bar',
      data: {
        labels: {{ labels_weeks }},
        datasets : [{
                  label: "Peak Traffic Volume",
                  data : {{ datas_weeks }},
                  fill: false,
                  lineTension: 0.1,
                  backgroundColor: "rgba(75,177,224,0.7)",
                  borderColor: "#fff",
                  borderCapStyle: 'butt',
                  borderDash: [],
                  borderDashOffset: 0.0,
                  borderJoinStyle: 'miter',
                  pointBorderColor: "rgba(75,192,192,1)",
                  pointBackgroundColor: "#fff",
                  pointBorderWidth: 1,
                  pointHoverRadius: 5,
                  pointHoverBackgroundColor: "rgba(75,192,192,1)",
                  pointHoverBorderColor: "rgba(220,220,220,1)",
                  pointHoverBorderWidth: 2,
                  pointRadius: 1,
                  pointHitRadius: 10,
                  spanGaps: false
              }]
      },
      options: {
                  legend: {
                            display: true,
                            labels: {
                                fontColor: 'rgb(255, 99, 132)',
                                fontSize : 18,
                            }
                        },
                    scales: {
                        yAxes: [{
                            scaleLabel :{
                                display: true,
                                labelString: 'Peak Number of vehicle / hr',
                                fontSize : 15,
                                fontColor : "#cf3408",
                            },
                            ticks: {
                                beginAtZero: true,
                                fontColor: "#ffa500"
                            }
                        }],
                        xAxes: [{
                            //gridLines: {
                            //	display: true,
                            //	color : "#606060",
                            //},
                            scaleLabel :{
                                display: true,
                                labelString: 'Weekly Days',
                                fontSize : 15,
                                fontColor : "#cf3408",
                            },
                            ticks: {
                                fontColor: "#ffa500",
                            }
                        }],
                    },
                },
      });
