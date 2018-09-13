# Event Durations

An event is defined as the transition process from one state to another state, which are determined by the value of the progress coordinate. In particular, the event duration is the time between occupying the former state for the last time and the later state for the first time. The analysis given here is designed such that the later state is the target state (or sink) of a non-equilibrium steady-state WESTPA simulation, i.e. the events under consideration lead to a recycling of the simulation replica upon finishing.

The two scripts work by extracting all relevant trajectory traces and subsequently providing a list of all event durations with their corresponding weight at the time of reaching the target state. More specifically, 'GetTraces.py' extracts all traces from a given 'west.h5' file in the same directory and saves the output '.txt' (and '.h5') files in the subdirectory 'Traces', which is created at run time. 'GetEvents.py' interrogates these traces and returns the output file 'Events_\*.dat', which is specific with respect to the progress coordinate of the event start.

**Example**<br />
<em>python GetTraces.py &nbsp;&nbsp; 800 &nbsp;&nbsp; 1200 &nbsp;&nbsp; 1</em><br />
(This uses 'w_trace' to write out traces of all events that end in a bin with 'pcoord < 1' between iteration number 800 and 1200.)<br />
<em>python GetEvents.py &nbsp;&nbsp; 800 &nbsp;&nbsp; 1200 &nbsp;&nbsp; 1 &nbsp;&nbsp; 4 &nbsp;&nbsp; 0.01</em><br />
(This interrogates the files created above with respect to events starting at 'pcoord >= 4' and determines the actual time by setting the iterative resampling time to 0.01.)
