#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init
use_plugin("python.core")
use_plugin('pypi:pybuilder_pytest')
use_plugin('pypi:pybuilder_pytest_coverage')
use_plugin("python.flake8")
use_plugin("python.distutils")
use_plugin("python.install_dependencies")
use_plugin("python.pycharm")
name = "schemamatcher-spark-duplicate"
default_task = ["install_dependencies", "publish"]

@init
def set_properties(project):
    project.version = "0.1"
    project.set_property("distutils_upload_repository", "http://insmtools04:8081/repository/pydev/")
    project.set_property('install_dependencies_extra_index_url', 'http://insmtools04:8081/repository/pydev/simple')
    project.set_property('install_dependencies_trusted_host', 'insmtools04')
    project.get_property("pytest_extra_args").append("--cov-report")
    project.get_property("pytest_extra_args").append("xml:tests/cov.xml")
    project.depends_on("pandas")
    project.depends_on("nltk")
    project.depends_on("py_stringmatching")
    project.depends_on("pyspark==3.0.1")
    project.build_depends_on("mock")
