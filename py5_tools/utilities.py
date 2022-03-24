# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2022 Jim Schmitz
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
import os
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

POM_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>py5</groupId>
  <artifactId>py5utilities</artifactId>
  <version>0.1</version>

  <name>py5utilities</name>
  <url>https://py5.ixora.io/</url>
  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
    <jarlocation>{classpath}</jarlocation>
  </properties>

  <dependencies>
    <dependency>
      <groupId>py5</groupId>
      <artifactId>py5-processing4</artifactId>
      <version>0.7.1a6</version>
      <scope>system</scope>
      <systemPath>${{jarlocation}}/core.jar</systemPath>
    </dependency>
    <dependency>
      <groupId>py5</groupId>
      <artifactId>py5-jogl</artifactId>
      <version>0.7.1a6</version>
      <scope>system</scope>
      <systemPath>${{jarlocation}}/jogl-all.jar</systemPath>
    </dependency>
    <dependency>
      <groupId>py5</groupId>
      <artifactId>py5</artifactId>
      <version>0.7.1a6</version>
      <scope>system</scope>
      <systemPath>${{jarlocation}}/py5.jar</systemPath>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-dependency-plugin</artifactId>
        <version>3.2.0</version>
        <executions>
          <execution>
            <id>copy</id>
            <phase>package</phase>
            <goals>
              <goal>copy</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <artifactItems>
            <artifactItem>
              <groupId>py5</groupId>
              <artifactId>py5utilities</artifactId>
              <version>0.1</version>
              <type>jar</type>
              <overWrite>true</overWrite>
              <outputDirectory>${{project.basedir}}/../jars</outputDirectory>
              <destFileName>py5utilities.jar</destFileName>
            </artifactItem>
          </artifactItems>
        </configuration>
      </plugin>
    </plugins>
  </build>

</project>
"""


def generate_utilities_framework(output_dir=None):
    java_dir = Path(output_dir or '.') / 'java'
    jars_dir = Path(output_dir or '.') / 'jars'

    import py5_tools
    py5_classpath = (
        Path(
            py5_tools.__file__).parent.parent /
        'py5/jars').as_posix()

    if 'CONDA_PREFIX' in os.environ and py5_classpath.startswith(
            os.environ['CONDA_PREFIX']):
        py5_classpath = py5_classpath.replace(
            os.environ['CONDA_PREFIX'], '${env.CONDA_PREFIX}')

    java_dir.mkdir(parents=True, exist_ok=True)
    jars_dir.mkdir(exist_ok=True)

    with open(java_dir / 'pom.xml', 'w') as f:
        f.write(POM_TEMPLATE.format(classpath=py5_classpath))

    utils_filename = java_dir / \
        Path('src/main/java/py5/utils/Py5Utilities.java')
    utils_filename.parent.mkdir(parents=True, exist_ok=True)
    with open(utils_filename, 'w') as f:
        f.write(PY5_UTILITIES_CLASS)


__all__ = ['generate_utilities_framework']
