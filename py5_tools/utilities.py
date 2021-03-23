# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2021 Jim Schmitz
#
#   This library is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published by
#   the Free Software Foundation, either version 2.1 of the License, or (at
#   your option) any later version.
#
#   This library is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
#   General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public License
#   along with this library. If not, see <https://www.gnu.org/licenses/>.
#
# *****************************************************************************
from pathlib import Path


PY5_UTILITIES_CLASS = """package py5.utils;

import py5.core.Sketch;

class Py5Utilities {

  public Sketch sketch;

  public Py5Utilities(Sketch sketch) {
    this.sketch = sketch;
  }

}
"""

DOT_PROJECT = """<?xml version="1.0" encoding="UTF-8"?>
<projectDescription>
	<name>py5utilities</name>
	<comment></comment>
	<projects>
	</projects>
	<buildSpec>
		<buildCommand>
			<name>org.eclipse.jdt.core.javabuilder</name>
			<arguments>
			</arguments>
		</buildCommand>
	</buildSpec>
	<natures>
		<nature>org.eclipse.jdt.core.javanature</nature>
	</natures>
	<filteredResources>
		<filter>
			<id>1599075320853</id>
			<name></name>
			<type>30</type>
			<matcher>
				<id>org.eclipse.core.resources.regexFilterMatcher</id>
				<arguments>node_modules|.git|__CREATED_BY_JAVA_LANGUAGE_SERVER__</arguments>
			</matcher>
		</filter>
	</filteredResources>
</projectDescription>
"""

DOT_CLASSPATH_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<classpath>
	<classpathentry kind="con" path="org.eclipse.jdt.launching.JRE_CONTAINER/org.eclipse.jdt.internal.debug.ui.launcher.StandardVMType/JavaSE-11"/>
	<classpathentry kind="src" path="src"/>
	<classpathentry kind="lib" path="{path}/core.jar"/>
	<classpathentry kind="lib" path="{path}/jogl-all.jar"/>
	<classpathentry kind="lib" path="{path}/py5.jar"/>
	<classpathentry kind="output" path="build"/>
</classpath>
"""

BUILD_XML_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<project name="py5 jar" default="dist">

    <description>
        compile and build the py5 utilities jar.
    </description>

    <property name="src" location="src"/>
    <property name="build" location="build"/>
    <property name="dist" location="{jars}"/>

    <target name="compile" description="compile the source">
        <mkdir dir="{build}"/>
        <javac source="11" target="11" debug="true" includeantruntime="false" srcdir="{src}" destdir="{build}">
            <classpath>
                <fileset dir="{path}">
                        <include name="**/*.jar"/>
                </fileset>
            </classpath>
        </javac>
    </target>

    <target name="dist" depends="compile" description="make the jar">
        <mkdir dir="{dist}"/>
        <jar destfile="{dist}/py5utilities.jar" basedir="{build}"/>
    </target>

    <target name="clean">
        <delete dir="{build}"/>
        <delete dir="{dist}"/>
    </target>

</project>
"""


def generate_utilities_framework(output_dir=None, jars_dir=None):
    output_path = Path(output_dir or '')
    ant_build_path = Path(jars_dir or 'jars')

    import py5
    py5_classpath = Path(py5.__file__).parent / 'jars'

    template_params = {
        x: f'{chr(36)}{{{x}}}' for x in [
            'build', 'dist', 'src']}
    template_params['path'] = py5_classpath.as_posix()
    template_params['jars'] = ant_build_path.absolute(
    ).as_posix() if output_dir else ant_build_path.as_posix()

    output_path.mkdir(parents=True, exist_ok=True)

    with open(output_path / 'build.xml', 'w') as f:
        f.write(BUILD_XML_TEMPLATE.format(**template_params))

    with open(output_path / '.classpath', 'w') as f:
        f.write(DOT_CLASSPATH_TEMPLATE.format(**template_params))

    with open(output_path / '.project', 'w') as f:
        f.write(DOT_PROJECT)

    src_dir = output_path / Path('src/py5/utils')
    src_dir.mkdir(parents=True, exist_ok=True)
    with open(src_dir / 'Py5Utilities.java', 'w') as f:
        f.write(PY5_UTILITIES_CLASS)


__all__ = ['generate_utilities_framework']
