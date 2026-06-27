---
sourceFile: "Using IPython for parallel computing — ipyparallel 9.2.1.dev documentation"
exportedBy: "Kortex"
exportDate: "2026-06-26T04:27:51.666Z"
---

# Using IPython for parallel computing — ipyparallel 9.2.1.dev documentation

c6d9bfb6-dfd5-4bfc-8a7d-17bdf9d90593

Using IPython for parallel computing — ipyparallel 9.2.1.dev documentation

119a3f4a-6173-4ff1-aecf-539e3a5982ec

https://ipyparallel.readthedocs.io/en/latest/

Using IPython for parallel computing — ipyparallel 9.2.1.dev documentation

Skip to main content

https://ipyparallel.readthedocs.io/en/latest/#main-content

Back to top

ipyparallel 9.2.1.dev documentation

https://ipyparallel.readthedocs.io/en/latest/

https://ipyparallel.readthedocs.io/en/latest/tutorial/index.html

https://ipyparallel.readthedocs.io/en/latest/reference/index.html

https://ipyparallel.readthedocs.io/en/latest/examples/index.html

https://ipyparallel.readthedocs.io/en/latest/changelog.html

API Reference

https://ipyparallel.readthedocs.io/en/latest/api/ipyparallel.html

https://github.com/ipython/ipyparallel

https://ipyparallel.readthedocs.io/en/latest/tutorial/index.html

https://ipyparallel.readthedocs.io/en/latest/reference/index.html

https://ipyparallel.readthedocs.io/en/latest/examples/index.html

https://ipyparallel.readthedocs.io/en/latest/changelog.html

API Reference

https://ipyparallel.readthedocs.io/en/latest/api/ipyparallel.html

https://github.com/ipython/ipyparallel

This isn't a stack. It's a pile. Errors, perf, logs, hosts. One tool, one bill, built 4 devs who ship

https://server.ethicalads.io/proxy/click/10510/019f0193-150b-7c81-bf1a-5d7920879e7a/

Ad by EthicalAds

https://www.ethicalads.io/advertisers/topics/data-science/?ref=rtd-sidebar-buy-ads

Using IPython for parallel computing

https://ipyparallel.readthedocs.io/en/latest/#using-ipython-for-parallel-computing

Jun 10, 2026

Installing IPython Parallel

https://ipyparallel.readthedocs.io/en/latest/#installing-ipython-parallel

As of 4.0, IPython parallel is now a standalone package called

ipyparallel

https://ipyparallel.readthedocs.io/en/latest/api/ipyparallel.html#module-ipyparallel

. You can install it with:

pip install ipyparallel

conda install ipyparallel

As of IPython Parallel 7, this will include installing/enabling an extension for both the classic Jupyter Notebook and JupyterLab ≥ 3.0.

https://ipyparallel.readthedocs.io/en/latest/#quickstart

IPython Parallel

#### A quick example to:

allocate a cluster (collection of IPython engines for use in parallel)

run a collection of tasks on the cluster

wait interactively for results

cleanup resources after the task is done

import time
import ipyparallel as ipp

task\_durations = \[1\] \* 25
# request a cluster
with ipp.Cluster() as rc:
    # get a view on the cluster
    view = rc.load\_balanced\_view()
    # submit the tasks
    asyncresult = view.map\_async(time.sleep, task\_durations)
    # wait interactively for results
    asyncresult.wait\_interactive()
    # retrieve actual results
    result = asyncresult.get()
# at this point, the cluster processes have been shutdown

You can similarly run MPI code using IPyParallel (requires

https://mpi4py.readthedocs.io/en/stable/install.html

import ipyparallel as ipp

def mpi\_example():
    from mpi4py import MPI
    comm = MPI.COMM\_WORLD
    return f"Hello World from rank {comm.Get\_rank()}. total ranks={comm.Get\_size()}"

# request an MPI cluster with 4 engines
with ipp.Cluster(engines='mpi', n=4) as rc:
    # get a broadcast\_view on the cluster which is best
    # suited for MPI style computation
    view = rc.broadcast\_view()
    # run the mpi\_example function on all engines in parallel
    r = view.apply\_sync(mpi\_example)
    # Retrieve and print the result from the engines
    print("\n".join(r))
# at this point, the cluster processes have been shutdown

https://ipyparallel.readthedocs.io/en/latest/tutorial/index.html

to learn more.

https://ipyparallel.readthedocs.io/en/latest/#contents

https://ipyparallel.readthedocs.io/en/latest/tutorial/index.html

Overview and getting started

https://ipyparallel.readthedocs.io/en/latest/tutorial/intro.html

Starting the IPython controller and engines

https://ipyparallel.readthedocs.io/en/latest/tutorial/process.html

IPython's Direct interface

https://ipyparallel.readthedocs.io/en/latest/tutorial/direct.html

The IPython task interface

https://ipyparallel.readthedocs.io/en/latest/tutorial/task.html

The AsyncResult object

https://ipyparallel.readthedocs.io/en/latest/tutorial/asyncresult.html

Parallel examples

https://ipyparallel.readthedocs.io/en/latest/tutorial/demos.html

https://ipyparallel.readthedocs.io/en/latest/reference/index.html

Using MPI with IPython

https://ipyparallel.readthedocs.io/en/latest/reference/mpi.html

IPython's Task Database

https://ipyparallel.readthedocs.io/en/latest/reference/db.html

Security details of IPython Parallel

https://ipyparallel.readthedocs.io/en/latest/reference/security.html

DAG Dependencies

https://ipyparallel.readthedocs.io/en/latest/reference/dag\_dependencies.html

Details of Parallel Computing with IPython

https://ipyparallel.readthedocs.io/en/latest/reference/details.html

Messaging for Parallel Computing

https://ipyparallel.readthedocs.io/en/latest/reference/messages.html

Connection Diagrams of The IPython ZMQ Cluster

https://ipyparallel.readthedocs.io/en/latest/reference/connections.html

https://ipyparallel.readthedocs.io/en/latest/reference/launchers.html

https://ipyparallel.readthedocs.io/en/latest/examples/index.html

https://ipyparallel.readthedocs.io/en/latest/examples/index.html#tutorials

https://ipyparallel.readthedocs.io/en/latest/examples/index.html#id1

Integrating IPython Parallel with other tools

https://ipyparallel.readthedocs.io/en/latest/examples/index.html#integrating-ipython-parallel-with-other-tools

Non-notebook examples

https://ipyparallel.readthedocs.io/en/latest/examples/index.html#non-notebook-examples

https://ipyparallel.readthedocs.io/en/latest/changelog.html

IPython Parallel API

https://ipyparallel.readthedocs.io/en/latest/#ipython-parallel-api

API Reference

https://ipyparallel.readthedocs.io/en/latest/api/ipyparallel.html

version\_info

https://ipyparallel.readthedocs.io/en/latest/api/ipyparallel.html#ipyparallel.version\_info

https://ipyparallel.readthedocs.io/en/latest/api/ipyparallel.html#classes

https://ipyparallel.readthedocs.io/en/latest/api/ipyparallel.html#decorators

https://ipyparallel.readthedocs.io/en/latest/api/ipyparallel.html#exceptions

Indices and tables

https://ipyparallel.readthedocs.io/en/latest/#indices-and-tables

https://ipyparallel.readthedocs.io/en/latest/genindex.html

Module Index

https://ipyparallel.readthedocs.io/en/latest/py-modindex.html

Search Page

https://ipyparallel.readthedocs.io/en/latest/search.html

next Tutorial

https://ipyparallel.readthedocs.io/en/latest/tutorial/index.html

On this page

Using IPython for parallel computing

https://ipyparallel.readthedocs.io/en/latest/

Installing IPython Parallel

https://ipyparallel.readthedocs.io/en/latest/#installing-ipython-parallel

https://ipyparallel.readthedocs.io/en/latest/#quickstart

https://ipyparallel.readthedocs.io/en/latest/#contents

IPython Parallel API

https://ipyparallel.readthedocs.io/en/latest/#ipython-parallel-api

Indices and tables

https://ipyparallel.readthedocs.io/en/latest/#indices-and-tables

Show Source

https://ipyparallel.readthedocs.io/en/latest/\_sources/index.md.txt

© Copyright The IPython Development Team.

Created using

https://www.sphinx-doc.org/

Built with the

PyData Sphinx Theme

https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html

https://ipyparallel.readthedocs.io/en/stable/

https://ipyparallel.readthedocs.io/en/9.2.0/

https://ipyparallel.readthedocs.io/en/9.1.0/

https://ipyparallel.readthedocs.io/en/9.0.2/

https://ipyparallel.readthedocs.io/en/9.0.1/

https://ipyparallel.readthedocs.io/en/9.0.0/

https://ipyparallel.readthedocs.io/en/8.8.0/

https://ipyparallel.readthedocs.io/en/8.7.0/

https://ipyparallel.readthedocs.io/en/8.6.1/

https://ipyparallel.readthedocs.io/en/8.6.0/

https://ipyparallel.readthedocs.io/en/8.5.0/

https://ipyparallel.readthedocs.io/en/8.4.1/

https://ipyparallel.readthedocs.io/en/8.4.0/

https://ipyparallel.readthedocs.io/en/8.3.0/

https://ipyparallel.readthedocs.io/en/8.2.0/

https://ipyparallel.readthedocs.io/en/8.1.0/

https://ipyparallel.readthedocs.io/en/8.0.0/

https://ipyparallel.readthedocs.io/en/7.1.0/

https://ipyparallel.readthedocs.io/en/7.0.1/

https://ipyparallel.readthedocs.io/en/7.0.0/

https://ipyparallel.readthedocs.io/en/6.2.3/

https://ipyparallel.readthedocs.io/en/6.2.2/

https://ipyparallel.readthedocs.io/en/6.2.1/

https://ipyparallel.readthedocs.io/en/6.2.0/

https://ipyparallel.readthedocs.io/en/6.1.1/

https://ipyparallel.readthedocs.io/en/6.1.0/

https://ipyparallel.readthedocs.io/en/6.0.2/

https://ipyparallel.readthedocs.io/en/6.0.1/

https://ipyparallel.readthedocs.io/en/5.2.0/

https://ipyparallel.readthedocs.io/en/5.1.1/

https://ipyparallel.readthedocs.io/en/5.1.0/

https://ipyparallel.readthedocs.io/en/5.0.1/

https://ipyparallel.readthedocs.io/en/5.0.0/

On Read the Docs

Project Home

https://app.readthedocs.org/projects/ipyparallel/?utm\_source=ipyparallel&utm\_content=flyout

https://app.readthedocs.org/projects/ipyparallel/builds/?utm\_source=ipyparallel&utm\_content=flyout

Addons documentation

https://docs.readthedocs.io/page/addons.html?utm\_source=ipyparallel&utm\_content=flyout

― Hosted by

Read the Docs

https://about.readthedocs.com/?utm\_source=ipyparallel&utm\_content=flyout

No recent searches

to navigate

Search powered by

