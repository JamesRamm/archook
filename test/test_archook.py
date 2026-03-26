import unittest
from unittest import mock

from archook import archook


class LocateProPythonZipTests(unittest.TestCase):
    def test_returns_none_when_python_zip_is_missing(self):
        with mock.patch.object(archook.glob, "glob", return_value=[]):
            self.assertIsNone(archook.locate_pro_python_zip(r"C:\ArcGIS\Pro\env"))

    def test_returns_first_sorted_python_zip_match(self):
        matches = [
            r"C:\ArcGIS\Pro\env\python311.zip",
            r"C:\ArcGIS\Pro\env\python310.zip",
        ]
        with mock.patch.object(archook.glob, "glob", return_value=matches):
            self.assertEqual(
                archook.locate_pro_python_zip(r"C:\ArcGIS\Pro\env"),
                r"C:\ArcGIS\Pro\env\python310.zip",
            )


class GetProPathsTests(unittest.TestCase):
    @mock.patch("archook.archook.locate_pro_python_zip")
    @mock.patch("archook.archook.locate_pro_conda")
    @mock.patch("archook.archook.locate_arcgis")
    @mock.patch("archook.archook.os.path.exists")
    def test_omits_missing_python_zip_and_filters_missing_paths(
        self, mock_exists, mock_locate_arcgis, mock_locate_pro_conda, mock_locate_pro_python_zip
    ):
        pro_dir = r"C:\ArcGIS\Pro"
        conda_dir = r"C:\ArcGIS\Pro\bin\Python\envs\arcgispro-py3"
        mock_locate_arcgis.return_value = pro_dir
        mock_locate_pro_conda.return_value = conda_dir
        mock_locate_pro_python_zip.return_value = None

        existing_paths = {
            conda_dir,
            conda_dir + r"\Scripts",
            conda_dir + r"\DLLs",
            conda_dir + r"\lib",
            conda_dir + r"\lib\site-packages",
            conda_dir + r"\Library\bin",
            pro_dir + r"\bin",
            pro_dir + r"\bin\Python",
            pro_dir + r"\bin\Python\Library\bin",
            pro_dir + r"\Resources\ArcPy",
        }
        mock_exists.side_effect = lambda path: path in existing_paths

        winpaths, syspaths = archook.get_pro_paths()

        self.assertEqual(
            winpaths,
            [
                conda_dir,
                conda_dir + r"\Scripts",
                conda_dir + r"\Library\bin",
                pro_dir + r"\bin",
                pro_dir + r"\bin\Python",
                pro_dir + r"\bin\Python\Library\bin",
            ],
        )
        self.assertEqual(
            syspaths,
            [
                conda_dir,
                conda_dir + r"\DLLs",
                conda_dir + r"\lib",
                conda_dir + r"\lib\site-packages",
                pro_dir + r"\bin",
                pro_dir + r"\Resources\ArcPy",
            ],
        )

    @mock.patch("archook.archook.locate_pro_python_zip")
    @mock.patch("archook.archook.locate_pro_conda")
    @mock.patch("archook.archook.locate_arcgis")
    @mock.patch("archook.archook.os.path.exists")
    def test_includes_python_zip_when_present(
        self, mock_exists, mock_locate_arcgis, mock_locate_pro_conda, mock_locate_pro_python_zip
    ):
        pro_dir = r"C:\ArcGIS\Pro"
        conda_dir = r"C:\ArcGIS\Pro\bin\Python\envs\arcgispro-py3"
        python_zip = conda_dir + r"\python311.zip"
        mock_locate_arcgis.return_value = pro_dir
        mock_locate_pro_conda.return_value = conda_dir
        mock_locate_pro_python_zip.return_value = python_zip

        existing_paths = {
            conda_dir,
            conda_dir + r"\Scripts",
            conda_dir + r"\DLLs",
            conda_dir + r"\lib",
            conda_dir + r"\lib\site-packages",
            conda_dir + r"\Library\bin",
            python_zip,
            pro_dir + r"\bin",
            pro_dir + r"\bin\Python",
            pro_dir + r"\bin\Python\Library\bin",
            pro_dir + r"\bin\Python\Scripts",
            pro_dir + r"\bin\Python\condabin",
            pro_dir + r"\Resources\ArcPy",
            pro_dir + r"\Resources\ArcToolbox\Scripts",
        }
        mock_exists.side_effect = lambda path: path in existing_paths

        _, syspaths = archook.get_pro_paths()

        self.assertIn(python_zip, syspaths)
        self.assertEqual(syspaths[1], python_zip)


if __name__ == "__main__":
    unittest.main()
