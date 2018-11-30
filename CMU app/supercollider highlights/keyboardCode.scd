//A basic Supercollider script that maps keys to note values, easially transferable to synths and routable to external software and devices
//It's not super developed, as I got sucked into livecoding (FoxDot and TidalCycles)


////1 Creates the keyboard -> midi from keyboard codes
(
e = Dictionary.new;
~midi = Dictionary.new;
~keyBoard = [
	[ $z, 122 ],
	[ $s, 115 ],
	[ $x , 120 ],
	[ $d , 100 ],
	[ $c , 99 ],
	[ $v ,118 ],
	[ $g ,103 ],
	[ $b ,98 ],
	[ $h ,104 ],
	[ $n ,110 ],
	[ $j ,106 ],
	[ $m ,109 ],
	[ $q ,113 ],
	[ $2 ,50 ],
	[ $w ,119 ],
	[ $3 ,51 ],
	[ $e ,101 ],
	[ $r ,114 ],
	[ $5 ,53 ],
	[ $t ,116 ],
	[ $6 ,54 ],
	[ $y ,121 ],
	[ $7 ,55 ],
	[ $u ,117 ],
	[ $i ,105 ],
	[ $9 ,57 ],
	[ $o ,111 ],
	[ $0 ,48 ],
	[ $p ,112 ]]
;
~midi.putPairs(["," ,[-1,"control"], "." ,[1,"control"], "/", [nil, "toggle"]]);
//~midiBtns = Dictionary.newFrom(List["," ,[-1,"control"], "." ,[1,"control"]]);

~interval=0;
~keyBoard.do{
	arg i;
	i[0].postln;
	~interval.postln;
	~midi.put(i[0].asString, [~interval, "note"]);
	~interval = ~interval+1;
};

~oct = 0;
~synth = \tone;
~currentNote = 0;
)


(
w = Window.new("I catch keystrokes");
~oct = 0;
~toggle = 1;
w.view.keyDownAction_({ arg view, char;
	var type=~midi[char.asString][1], key=~midi[char.asString][0];

	~toggle.postln;
	key.postln;
	if( type == "note" || ~toggle == 1, {
		var sig,env, note;
		"in".postln;
		note = 12 * ~oct + key + 60 ;
		(instrument: ~synth, freq: note.midicps, octave: ~oct).play;
	}.play, {(instrument: ~synth)}.stop);
	if( type == "control" , {~oct = ~oct + key; ~oct.postln});
	if( type == "toggle" , {~toggle = ~toggle%2 + 1; ~toggle.postln});
	type.postln;
});

w.front;
)



(
SynthDef.new(\tone, {
		arg freq=440, amp=0.3;
		var sig,env;
		sig = LFTri.ar(freq)!2;
		env = EnvGen.kr(Env.perc, doneAction:2);
		sig = sig * env * amp;
		Out.ar(0,sig);
		//.linexp maps linear values to an exponential range
}).add;
)
