This repository is meant to facilitate the benchmarking of fairness aware machine learning algorithms.

To run the benchmarks, clone the repository and run:

    $ python3 benchmark.py

This will write out metrics for each dataset to the results/ directory.

To generate graphs and other analysis run:

    $ python3 analysis.py

If you do not yet have all the packages installed, you may need to run:

    $ pip install -r requirements.txt

*Optional*:  The benchmarks rely on preprocessed versions of the datasets that have been included
in the repository.  If you would like to regenerate this preprocessing, run the below command
before running the benchmark script:

    $ python3 preprocess.py

To add new datasets or algorithms, see the instructions in the readme files in those directories.

## OS-specific things

### On Ubuntu

(We tested on Ubuntu 16.04, your mileage may vary)

You'll need `python3-dev`:

    $ sudo apt-get install python3-dev


### Additional analysis-specific requirements

To regenerate figures (this is messy right now. we're working on it)

Python requirements (use pip):

* `ggplot`

System requirements:

* `pandoc`  (`brew install pandoc` on a Mac or `apt-get install pandoc` on Linux)
* R

R package requirements (use `install.packages`):

* `stringr`
* `ggplot2`
* `dplyr`
* `magrittr`
* `corrplot`
* `robust`
