

var points1 = [
  [85.34957,27.67813], [85.34953,27.67907]
];
var points2 = [
  [85.34968,27.67905], [85.349685,27.67891], [85.34956,27.67884], [85.34944,27.67864], [85.34924,27.67853]
];

var points3 = [
  [85.34907,27.67847], [85.34942,27.67867],[85.34957,27.67868], [85.34965,27.67864], [85.34966,27.67862], [85.34967,27.67855], [85.34968,27.67850]
];

var points4 = [
  [85.34942,27.67867],[85.34950,27.67880], [85.34949,27.67907]
];

var points5 = [
  [85.349685,27.67891],[85.34969,27.67863], [85.34971,27.67850]
];
var points6 = [
  [85.34957,27.67816],[85.34943,27.67837], [85.34937,27.67841], [85.34929,27.67843], [85.34911,27.678435], [85.34903,27.67842], [85.34896,27.67838]
];

function arrowheadRotation(point){
var endPoint1 = point[point.length - 2]
var endPoint2 = point[point.length - 1]
var dx = endPoint2[0] - endPoint1[0];
var dy = endPoint2[1] - endPoint1[1];
var rotation = Math.atan2(dy, dx);
return rotation;
}
var rotation1 = arrowheadRotation(points1);
var rotation2 = arrowheadRotation(points2);
var rotation3 = arrowheadRotation(points3);
var rotation4 = arrowheadRotation(points4);
var rotation5 = arrowheadRotation(points5);
var rotation6 = arrowheadRotation(points6);

var route1 = new ol.geom.LineString(points1);
route1.transform('EPSG:4326', 'EPSG:3857');
var route2 = new ol.geom.LineString(points2);
route2.transform('EPSG:4326', 'EPSG:3857');
var route3 = new ol.geom.LineString(points3);
route3.transform('EPSG:4326', 'EPSG:3857');
var route4 = new ol.geom.LineString(points4);
route4.transform('EPSG:4326', 'EPSG:3857');
var route5 = new ol.geom.LineString(points5);
route5.transform('EPSG:4326', 'EPSG:3857');
var route6 = new ol.geom.LineString(points6);
route6.transform('EPSG:4326', 'EPSG:3857');

var routeFeature1 = new ol.Feature({
  type: 'route1',
  geometry: route1
});
var routeFeature2 = new ol.Feature({
  type: 'route2',
  geometry: route2
});
var routeFeature3 = new ol.Feature({
  type: 'route3',
  geometry: route3
});
var routeFeature4 = new ol.Feature({
  type: 'route4',
  geometry: route4
});
var routeFeature5 = new ol.Feature({
  type: 'route5',
  geometry: route5
});
var routeFeature6 = new ol.Feature({
  type: 'route6',
  geometry: route6
});

var startMarker1 = new ol.Feature({
  type: 'icon-a',
  geometry: new ol.geom.Point(ol.proj.fromLonLat(points1[0]))
});
var startMarker2 = new ol.Feature({
  type: 'icon-a',
  geometry: new ol.geom.Point(ol.proj.fromLonLat(points2[0]))
});
var startMarker3 = new ol.Feature({
  type: 'icon-a',
  geometry: new ol.geom.Point(ol.proj.fromLonLat(points3[0]))
});
var startMarker4 = new ol.Feature({
  type: 'icon-a',
  geometry: new ol.geom.Point(ol.proj.fromLonLat(points4[0]))
});
var startMarker5 = new ol.Feature({
  type: 'icon-a',
  geometry: new ol.geom.Point(ol.proj.fromLonLat(points5[0]))
});
var startMarker6 = new ol.Feature({
  type: 'icon-a',
  geometry: new ol.geom.Point(ol.proj.fromLonLat(points6[0]))
});

var endMarker1 = new ol.Feature({
  type: 'icon-b',
  geometry: new ol.geom.Point(ol.proj.fromLonLat(points1[points1.length - 1]))
});
var endMarker2 = new ol.Feature({
  type: 'icon-b',
  geometry: new ol.geom.Point(ol.proj.fromLonLat(points2[points2.length - 1]))
});
var endMarker3 = new ol.Feature({
  type: 'icon-b',
  geometry: new ol.geom.Point(ol.proj.fromLonLat(points3[points3.length - 1]))
});
var endMarker4 = new ol.Feature({
  type: 'icon-b',
  geometry: new ol.geom.Point(ol.proj.fromLonLat(points4[points4.length - 1]))
});
var endMarker5 = new ol.Feature({
  type: 'icon-b',
  geometry: new ol.geom.Point(ol.proj.fromLonLat(points5[points5.length - 1]))
});
var endMarker6 = new ol.Feature({
  type: 'icon-b',
  geometry: new ol.geom.Point(ol.proj.fromLonLat(points6[points6.length - 1]))
});

var stylesMap1 = {
  'route1': function(feature) {
    var geometry = feature.getGeometry();
    var styles = [
      // linestring
      new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: color_p2,
          width: 6
        }),
        image: new ol.style.Icon({
          anchor: [0.5, 0.5],
          src: "{{ url_for('static', filename='icon-a_50.png') }}"
        })
      })
    ];
    return styles;
  },
  'icon-a': new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.5, 0.5],
      src: "{{ url_for('static', filename='icon-a_50.png') }}"
    })
  }),
  'icon-b': new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.75, 0.5],
      src: "{{ url_for('static', filename='icon-b_50.png') }}",
      rotateWithView: true,
      rotation: -rotation1,

    })
  })
};

var stylesMap2 = {
  'route2': function(feature) {
    console.log('style map 2');
    console.log('color in styleMap2 =============>>>>>>>>' + color_p2);
    var geometry = feature.getGeometry();
    var styles = [
      // linestring
      new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: color_p1,
          width: 6
        }),
        image: new ol.style.Icon({
          anchor: [0.5, 0.5],
          src: "{{ url_for('static', filename='icon-a_50.png') }}"
        })
      })
    ];

    return styles;
  },
  'icon-a': new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.5, 0.5],
      src: "{{ url_for('static', filename='icon-a_50.png') }}"
    })
  }),
  'icon-b': new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.75, 0.5],
      src: "{{ url_for('static', filename='icon-b_50.png') }}",
      rotateWithView: true,
      rotation: -rotation2,

    })
  })
};
var stylesMap3 = {
  'route3': function(feature) {
    var geometry = feature.getGeometry();
    var styles = [
      // linestring
      new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: color_p3,
          width: 6
        }),
        image: new ol.style.Icon({
          anchor: [0.5, 0.5],
          src: "{{ url_for('static', filename='icon-a_50.png') }}"
        })
      })
    ];

    return styles;
  },
  'icon-a': new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.5, 0.5],
      src: "{{ url_for('static', filename='icon-a_50.png') }}"
    })
  }),
  'icon-b': new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.75, 0.5],
      src: "{{ url_for('static', filename='icon-b_50.png') }}",
      rotateWithView: true,
      rotation: -rotation3,

    })
  })
};
var stylesMap4 = {
  'route4': function(feature) {
    var geometry = feature.getGeometry();
    var styles = [
      // linestring
      new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: color_green,
          width: 6
        }),
        image: new ol.style.Icon({
          anchor: [0.5, 0.5],
          src: "{{ url_for('static', filename='icon-a_50.png') }}"
        })
      })
    ];

    return styles;
  },
  'icon-a': new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.5, 0.5],
      src: "{{ url_for('static', filename='icon-a_50.png') }}"
    })
  }),
  'icon-b': new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.75, 0.5],
      src: "{{ url_for('static', filename='icon-b_50.png') }}",
      rotateWithView: true,
      rotation: -rotation4,

    })
  })
};
var stylesMap5 = {

  'route5': function(feature) {
    var geometry = feature.getGeometry();
    var styles = [
      // linestring
      new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: color_green,
          width: 6
        }),
        image: new ol.style.Icon({
          anchor: [0.5, 0.5],
          src: "{{ url_for('static', filename='icon-a_50.png') }}"
        })
      })
    ];

    return styles;
  },
  'icon-a': new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.5, 0.5],
      src: "{{ url_for('static', filename='icon-a_50.png') }}"
    })
  }),
  'icon-b': new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.75, 0.5],
      src: "{{ url_for('static', filename='icon-b_50.png') }}",
      rotateWithView: true,
      rotation: -rotation5,

    })
  })
};
var stylesMap6 = {
  'route6': function(feature) {
    var geometry = feature.getGeometry();
    var styles = [
      // linestring
      new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: color_green,
          width: 6
        }),
        image: new ol.style.Icon({
          anchor: [0.5, 0.5],
          src: "{{ url_for('static', filename='icon-a_50.png') }}"
        })
      })
    ];

    return styles;
  },
  'icon-a': new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.5, 0.5],
      src: "{{ url_for('static', filename='icon-a_50.png') }}"
    })
  }),
  'icon-b': new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.75, 0.5],
      src: "{{ url_for('static', filename='icon-b_50.png') }}",
      rotateWithView: true,
      rotation: -rotation6,

    })
  })
};

var vectorLayer1 = new ol.layer.Vector({
  source: new ol.source.Vector({
    features: [routeFeature1, startMarker1, endMarker1]
  }),
  style: function(feature) {
    const myStyle = stylesMap1[feature.get('type')];
    if (myStyle instanceof Function) {
      return myStyle(feature);
    }
    return myStyle;
  }
});
var vectorLayer2 = new ol.layer.Vector({
  source: new ol.source.Vector({
    features: [routeFeature2, startMarker2, endMarker2]
  }),
  style: function(feature) {
    const myStyle = stylesMap2[feature.get('type')];
    if (myStyle instanceof Function) {
      return myStyle(feature);
    }
    return myStyle;
  }
});
var vectorLayer3 = new ol.layer.Vector({
  source: new ol.source.Vector({
    features: [routeFeature3, startMarker3, endMarker3]
  }),
  style: function(feature) {
    const myStyle = stylesMap3[feature.get('type')];
    if (myStyle instanceof Function) {
      return myStyle(feature);
    }
    return myStyle;
  }
});
var vectorLayer4 = new ol.layer.Vector({
  source: new ol.source.Vector({
    features: [routeFeature4, startMarker4, endMarker4]
  }),
  style: function(feature) {
    const myStyle = stylesMap4[feature.get('type')];
    if (myStyle instanceof Function) {
      return myStyle(feature);
    }
    return myStyle;
  }
});
var vectorLayer5 = new ol.layer.Vector({
  source: new ol.source.Vector({
    features: [routeFeature5, startMarker5, endMarker5]
  }),
  style: function(feature) {
    const myStyle = stylesMap5[feature.get('type')];
    if (myStyle instanceof Function) {
      return myStyle(feature);
    }
    return myStyle;
  }
});
var vectorLayer6 = new ol.layer.Vector({
  source: new ol.source.Vector({
    features: [routeFeature6, startMarker6, endMarker6]
  }),
  style: function(feature) {
    const myStyle = stylesMap6[feature.get('type')];
    if (myStyle instanceof Function) {
      return myStyle(feature);
    }
    return myStyle;
  }
});

var center = ol.proj.fromLonLat([85.34930, 27.67860]);
var map = new ol.Map({
  target: document.getElementById('map'),
  view: new ol.View({
    center: center,
    zoom: 18.1,
    // zoomFactor : 2.095,  //hit and trial,
    minZoom: 2,
    maxZoom: 25,
  }),
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM()
    }),
    vectorLayer1,
    vectorLayer2,
    vectorLayer3,
    vectorLayer4,
    vectorLayer5,
    vectorLayer6,
  ]
});