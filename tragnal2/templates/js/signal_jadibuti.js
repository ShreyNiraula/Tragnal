var color_red = '#ff2222';
var color_green = '#00FF00';
var color_p1 = color_red;
var color_p2 = color_red;
var color_p3 = color_red;
var counter=1;
var iteration=0;
var currentPhase=1;



    $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
    (function(){
        $.getJSON(
            $SCRIPT_ROOT+"/_imgJadibuti", // Your AJAX route here
            function(dota) {
                // Update the value in your table here
                if (dota.t1[0]) {
                console.log('inside phase cond of img t1 0');
                $('#traffic1').attr('src',"{{ url_for('static', filename='images/signals/r.png') }}");
                }

                if (dota.t1[1]) {
                console.log('inside phase cond of img t1 1');
                $('#traffic1').attr('src',"{{ url_for('static', filename='images/signals/y.png') }}");
                }


                if (dota.t1[2]){
                color_p1 = color_green;
                console.log('inside phase cond of img t1 2');
                $('#traffic1').attr('src',"{{ url_for('static', filename='images/signals/g.png') }}");
                }
                else
                {
                    color_p1 = color_red;
                }

                if (dota.t1[3]){
                console.log('inside phase cond of img t1 3');
                $('#traffic1').attr('src',"{{ url_for('static', filename='images/signals/s.png') }}");
                }

                if (dota.t2[0]){
                console.log('inside phase cond of img t2 0');
                $('#traffic2').attr('src',"{{ url_for('static', filename='images/signals/r.png') }}");
                }



                if (dota.t2[1]){
                console.log('inside phase cond of img t2 1');
                $('#traffic2').attr('src',"{{ url_for('static', filename='images/signals/y.png') }}");
                }

                if (dota.t2[2]){
                color_p2= color_green;
                console.log('inside phase cond of img t2 2');
                $('#traffic2').attr('src',"{{ url_for('static', filename='images/signals/g.png') }}");
                }

                if (dota.t2[3]){
                console.log('inside phase cond of img t2 3');
                $('#traffic2').attr('src',"{{ url_for('static', filename='images/signals/s.png') }}");
                }
                else
                {
                color_p2= color_red;
                }

                if (dota.t3[0]){
                console.log('inside phase cond of img t3 0');
                $('#traffic3').attr('src',"{{ url_for('static', filename='images/signals/r.png') }}");
                }

                if (dota.t3[1]){
                console.log('inside phase cond of img t3 1');
                $('#traffic3').attr('src',"{{ url_for('static', filename='images/signals/y.png') }}");
                }

                if (dota.t3[2]){

                console.log('inside phase cond of img t3 2');
                $('#traffic3').attr('src',"{{ url_for('static', filename='images/signals/g.png') }}");
                }
                else
                {
                color_p3=color_red;
                }

                if (dota.t3[3]){
                console.log('inside phase cond of img t3 3');
                $('#traffic3').attr('src',"{{ url_for('static', filename='images/signals/s.png') }}");
                }

                $("#counter1").text(dota.t1[4]);
                $("#counter2").text(dota.t2[4]);
                $("#counter3").text(dota.t3[4]);

                currentPhase = dota.phase_number;
                console.log('currentPhase '+currentPhase);
                $("#phase_number").text(currentPhase);

                if(currentPhase ==1)
                {
                $('#jphase').attr('src',"{{ url_for('static', filename='images/junctions/Jadibuti/jp1.png') }}");
                }
                else if(currentPhase==2)
                {
                $('#jphase').attr('src',"{{ url_for('static', filename='images/junctions/Jadibuti/jp2.png') }}");
                }
                else
                {
                $('#jphase').attr('src',"{{ url_for('static', filename='images/junctions/Jadibuti/jp3.png') }}");
                }
            });
        setTimeout(arguments.callee, 490);

        $("#nextphasebutton").off().on('click', function() {
        console.log('are you here?');
        $.getJSON('/_button_J',
                {state: currentPhase},
                function(data) {
                console.log('am within button JSON with current value of '+data.phase_number);
                currentPhase = data.phase_number;
                $("#phase_number_updated").text(currentPhase);
                if(currentPhase ==1)
                {
                $('#jphase').attr('src',"{{ url_for('static', filename='images/junctions/Jadibuti/jp1.png') }}");
                }
                else if(currentPhase==2)
                {
                $('#jphase').attr('src',"{{ url_for('static', filename='images/junctions/Jadibuti/jp2.png') }}");
                }
                else
                {
                $('#jphase').attr('src',"{{ url_for('static', filename='images/junctions/Jadibuti/jp3.png') }}");
                }

                }
                );
        });
      })();

