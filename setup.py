import setuptools

setuptools.setup(
  name="lisa",
  version="0.0.0",
  description="python project in docker",
  packages=setuptools.find_packages("src"),
  package_dir={"": "src"},
)
