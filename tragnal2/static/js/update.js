$(document).ready( function (){
    $('#red1').on('click', function() {
    $('my_image').attr('src',"{{ url_for('static', filename='pealeg,jpg') }}");
    })

    })
})


$(
    function()
    { if phase['t1'][0]
        {
            function()
            {
                $('#my_image').attr('src','second.jpg');
            }
        }
    }
  );

    $(
    function()
    {
    console.log('herhehrehrehr');

        $.getJSON('/_img',
                {
                    state: None
                },
                    function(data) {
                        $("#r_res").text(data.r_res);
                    }
                );

        });


$(
    function()
    { {%if phase['t2'][2]%}

        $.get("{{ url_for('account') }}", function(data, status){
    alert("Data: " + data + "\nStatus: " + status);
    $('#rImg2').attr('src',"{{ url_for('static', filename='r.png') }}");
        });


       {% endif %}
    }
  );





    $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
    (function(){
        $.getJSON(
            $SCRIPT_ROOT+"/account", // Your AJAX route here
            function(phase) {
                // Update the value in your table here
                {%if phase['t1'][0]%}
                console.log('inside phase cond of img t1 0');
                $('#traffic1').attr('src',"{{ url_for('static', filename='g.png') }}");
                {% endif %}

                {%if phase['t1'][1]%}
                console.log('inside phase cond of img t1 0');
                $('#traffic1').attr('src',"{{ url_for('static', filename='y.png') }}");
                {% endif %}

                {%if phase['t1'][2]%}
                console.log('inside phase cond of img t1 0');
                $('#traffic1').attr('src',"{{ url_for('static', filename='r.png') }}");
                {% endif %}

                {%if phase['t1'][3]%}
                console.log('inside phase cond of img t1 0');
                $('#traffic1').attr('src',"{{ url_for('static', filename='s.png') }}");
                {% endif %}

                {%if phase['t2'][0]%}
                console.log('inside phase cond of img t1 0');
                $('#traffic2').attr('src',"{{ url_for('static', filename='g.png') }}");
                {% endif %}

                {%if phase['t2'][1]%}
                console.log('inside phase cond of img t1 0');
                $('#traffic2').attr('src',"{{ url_for('static', filename='y.png') }}");
                {% endif %}

                {%if phase['t2'][2]%}
                console.log('inside phase cond of img t1 0');
                $('#traffic2').attr('src',"{{ url_for('static', filename='r.png') }}");
                {% endif %}

                {%if phase['t2'][3]%}
                console.log('inside phase cond of img t1 0');
                $('#traffic2').attr('src',"{{ url_for('static', filename='s.png') }}");
                {% endif %}


                {%if phase['t3'][0]%}
                console.log('inside phase cond of img t1 0');
                $('#traffic3').attr('src',"{{ url_for('static', filename='g.png') }}");
                {% endif %}

                {%if phase['t3'][1]%}
                console.log('inside phase cond of img t1 0');
                $('#traffic3').attr('src',"{{ url_for('static', filename='y.png') }}");
                {% endif %}

                {%if phase['t3'][2]%}
                console.log('inside phase cond of img t1 0');
                $('#traffic3').attr('src',"{{ url_for('static', filename='r.png') }}");
                {% endif %}

                {%if phase['t3'][3]%}
                console.log('inside phase cond of img t1 0');
                $('#traffic3').attr('src',"{{ url_for('static', filename='s.png') }}");
                {% endif %}
            })

        setTimeout(arguments.callee, 1000);
    })();

$( function () {
    $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
    (function(){
        console.log(' am outside getJson');
        $.getJSON(

            $SCRIPT_ROOT+"/_img", // Your AJAX route here

            function(dota) {

                // Update the value in your table here
                if (dota.t1[0]) {
                console.log('inside phase cond of img t1 0');
                $('#traffic1').attr('src',"{{ url_for('static', filename='g.png') }}");
                }

                if (dota.t1[1]) {
                console.log('inside phase cond of img t1 1');
                $('#traffic1').attr('src',"{{ url_for('static', filename='y.png') }}");
                }

                if (dota.t1[2]){
                console.log('inside phase cond of img t1 2');
                $('#traffic1').attr('src',"{{ url_for('static', filename='r.png') }}");
                }

                if (dota.t1[3]){
                console.log('inside phase cond of img t1 3');
                $('#traffic1').attr('src',"{{ url_for('static', filename='s.png') }}");
                }

                if (dota.t2[0]){
                console.log('inside phase cond of img t2 0');
                $('#traffic2').attr('src',"{{ url_for('static', filename='g.png') }}");
                }

                if (dota.t2[1]){
                console.log('inside phase cond of img t2 1');
                $('#traffic2').attr('src',"{{ url_for('static', filename='y.png') }}");
                }

                if (dota.t2[2]){
                console.log('inside phase cond of img t2 2');
                $('#traffic2').attr('src',"{{ url_for('static', filename='r.png') }}");
                }

                if (dota.t2[3]){
                console.log('inside phase cond of img t2 3');
                $('#traffic2').attr('src',"{{ url_for('static', filename='s.png') }}");
                }

                if (dota.t3[0]){
                console.log('inside phase cond of img t3 0');
                $('#traffic3').attr('src',"{{ url_for('static', filename='g.png') }}");
                }

                if (dota.t3[1]){
                console.log('inside phase cond of img t3 1');
                $('#traffic3').attr('src',"{{ url_for('static', filename='y.png') }}");
                }

                if (dota.t3[2]){
                console.log('inside phase cond of img t3 2');
                $('#traffic3').attr('src',"{{ url_for('static', filename='r.png') }}");
                }

                if (dota.t3[3]){
                console.log('inside phase cond of img t3 3');
                $('#traffic3').attr('src',"{{ url_for('static', filename='s.png') }}");
                }
            })
        setTimeout(arguments.callee, 3000);
    })();
});