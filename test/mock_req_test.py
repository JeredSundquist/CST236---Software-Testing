from source.main import Interface
from unittest import TestCase
from test.plugins.ReqTracer import requirements
import source.git_utils
from mock import patch, Mock
import os.path


class GetMockTestReq(TestCase):
    # mock file in repo = yes
    @patch('subprocess.Popen')
    @requirements(['#0100', '#0050', '#0051', '#0052'])
    def test_fileInRepo_Yes(self, mock_subproc_popen):
        obj = Interface()
        process_mock = Mock()
        attrs = {'communicate.return_value': ('', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = obj.ask('Is the <nose2.cfg> in the repo?')
        self.assertEqual(result, 'Yes')

    # mock file in repo = no
    @patch('subprocess.Popen')
    @requirements(['#0100', '#0050', '#0051', '#0052'])
    def test_fileInRepo_No(self, mock_subproc_popen):
        obj = Interface()
        process_mock = Mock()
        attrs = {'communicate.return_value': ('test.txt', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = obj.ask('Is the <test.txt> in the repo?')
        self.assertEqual(result, 'No')

    # mock file status = modified
    @patch('source.git_utils.get_diff_files')
    @requirements(['#0101', '#0050', '#0051', '#0052'])
    def test_fileStatus_Modified(self, mock_subproc_diff_files):
        obj = Interface()
        mock_subproc_diff_files.return_value = os.path.abspath('requirements.txt')
        result = obj.ask('What is the status of <requirements.txt>?')
        self.assertEqual(result, 'requirements.txt has been modified locally')

    # mock file status = un-tracked
    @patch('source.git_utils.get_diff_files')
    @patch('source.git_utils.get_untracked_files')
    @requirements(['#0101', '#0050', '#0051', '#0052'])
    def test_fileStatus_Untracked(self, mock_untracked, mock_diff):
        obj = Interface()
        mock_diff.return_value = []
        mock_untracked.return_value = os.path.abspath('requirements.txt')
        result = obj.ask('What is the status of <requirements.txt>?')
        self.assertEqual(result, 'requirements.txt has not been checked in')

    # mock file status = dirty
    @patch('source.git_utils.get_diff_files')
    @patch('source.git_utils.get_untracked_files')
    @patch('source.git_utils.is_repo_dirty')
    @requirements(['#0101', '#0050', '#0051', '#0052'])
    def test_fileStatus_Dirty(self, mock_dirty, mock_untracked, mock_diff):
        obj = Interface()
        mock_diff.return_value = []
        mock_dirty.return_value = True
        mock_untracked.return_value = []
        result = obj.ask('What is the status of <requirements.txt>?')
        self.assertEqual(result, 'requirements.txt is a dirty repo')

    # mock file info
    @patch('subprocess.Popen')
    @requirements(['#0102', '#0050', '#0051', '#0052'])
    def test_file_info(self, mock_subproc_popen):
        obj = Interface()
        process_mock = Mock()
        attrs = {'communicate.return_value': ('__file__', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = obj.ask('What is the deal with <{}>?'.format(__file__))
        self.assertEqual(result, '__file__')

    # mock repo branch
    @patch('subprocess.Popen')
    @requirements(['#0103', '#0050', '#0051', '#0052'])
    def test_repo_branch(self, mock_subproc_popen):
        obj = Interface()
        process_mock = Mock()
        attrs = {'communicate.return_value': ('__file__', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = obj.ask('What branch is <{}>?'.format(__file__))
        self.assertEqual(result, '__file__')

    # mock repo url
    @patch('subprocess.Popen')
    @requirements(['#0104', '#0050', '#0051', '#0052'])
    def test_repo_url(self, mock_subproc_popen):
        obj = Interface()
        process_mock = Mock()
        attrs = {'communicate.return_value': ('__file__', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = obj.ask('Where did <{}> come from?'.format(__file__))
        self.assertEqual(result, '__file__')

    # Coverage_________________________________________________________________________________________________________
    # bad path
    @requirements(['#0050', '#0051', '#0052'])
    def test_path_checker(self):
        self.assertRaisesRegexp(Exception, 'Path blah does not exist cannot get git file',
                                source.git_utils.get_git_file_info, 'blah')

    # mock is file in repo = changed or untracked
    @patch('source.git_utils.is_file_in_repo')
    @patch('source.git_utils.get_untracked_files')
    @requirements(['#0100', '#0050', '#0051', '#0052'])
    def test_fileStatus_NotDirty(self, mock_untracked, mock_is_file_in_repo):
        obj = Interface()
        mock_untracked.return_value = os.path.abspath('requirements.txt')
        mock_is_file_in_repo.return_value = 'No'
        result = obj.ask('Is the <requirements.txt> in the repo?')
        self.assertEqual(result, 'No')

    # mock get git file info = is up to date
    @patch('source.git_utils.get_diff_files')
    @patch('source.git_utils.get_untracked_files')
    @patch('source.git_utils.is_repo_dirty')
    @requirements(['#0101', '#0050', '#0051', '#0052'])
    def test_get_git_file_info_upToDate(self, mock_is_repo_dirty, mock_get_untracked_files, mock_get_diff_files):
        obj = Interface()
        mock_get_diff_files.return_value = []
        mock_get_untracked_files.return_value = []
        mock_is_repo_dirty.return_value = False
        result = obj.ask('What is the status of <requirements.txt>?')
        self.assertEqual(result, 'requirements.txt is up to date')

    # mock git execute with stderr
    @patch('subprocess.Popen')
    @requirements(['#0104', '#0050', '#0051', '#0052'])
    def test_git_execute_stderr(self, mock_subproc_popen):
        obj = Interface()
        process_mock = Mock()
        attrs = {'communicate.return_value': ('__file__', 'blah')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = obj.ask('Where did <{}> come from?'.format(__file__))
        self.assertEqual(result, '__file__')

    # mock is repo dirty = true
    @patch('source.git_utils.has_diff_files')
    @requirements(['#0050', '#0051', '#0052'])
    def test_is_repo_dirtyTrue(self, mock_has_diff_files):
        mock_has_diff_files.return_value = __file__
        result = source.git_utils.is_repo_dirty(__file__)
        self.assertEqual(result, True)

    # mock is repo dirty = false
    @patch('source.git_utils.has_diff_files')
    @requirements(['#0050', '#0051', '#0052'])
    def test_is_repo_dirtyFalse(self, mock_has_diff_files):
        mock_has_diff_files.return_value = False
        result = source.git_utils.is_repo_dirty(__file__)
        self.assertEqual(result, False)

    # mock has diff files = true
    @patch('source.git_utils.get_diff_files')
    @requirements(['#0050', '#0051', '#0052'])
    def test_has_diff_filesTrue(self, mock_get_diff_files):
        mock_get_diff_files.return_value = __file__
        result = source.git_utils.is_repo_dirty(__file__)
        self.assertEqual(result, True)

    # mock has diff files = false
    @patch('source.git_utils.get_diff_files')
    @requirements(['#0050', '#0051', '#0052'])
    def test_has_diff_filesFalse(self, mock_get_diff_files):
        mock_get_diff_files.return_value = []
        result = source.git_utils.is_repo_dirty(__file__)
        self.assertEqual(result, False)

    # mock has untracked files = true
    @patch('source.git_utils.get_untracked_files')
    @requirements(['#0050', '#0051', '#0052'])
    def test_has_untracked_filesTrue(self, mock_get_untracked_files):
        mock_get_untracked_files.return_value = __file__
        result = source.git_utils.has_untracked_files(__file__)
        self.assertEqual(result, True)

    # mock has untracked files = false
    @patch('source.git_utils.get_untracked_files')
    @requirements(['#0050', '#0051', '#0052'])
    def test_has_untracked_filesFalse(self, mock_get_untracked_files):
        mock_get_untracked_files.return_value = []
        result = source.git_utils.has_untracked_files(__file__)
        self.assertEqual(result, False)

    # mock get repo root path for get diff files
    @patch('source.git_utils.git_execute')
    @patch('os.path.exists')
    @requirements(['#0050', '#0051', '#0052'])
    def test_get_repo_root_path_get_diff_files(self, mock_os_path, mock_git_execute):
        mock_os_path.return_value = True
        mock_git_execute.return_value = os.path.abspath(__file__)
        result = source.git_utils.is_file_in_repo(__file__)
        self.assertEqual(result, 'No')

    # mock get repo root path for get untracked files
    @patch('subprocess.Popen')
    @requirements(['#0050', '#0051', '#0052'])
    def test_get_repo_root_path_get_untracked_files(self, mock_subproc_popen):
        process_mock = Mock()
        attrs = {'communicate.side_effect': [('', 'empty'), ('', 'empty'), ('git_utils_test.py', 'onlyFile'),
                                             (__file__, '4'), ('something', '5'), ('maybe', '6')]}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.is_file_in_repo(os.path.relpath(__file__))
        self.assertEqual(result, 'Yes')

    # mock get repo root path
    @patch('source.git_utils.git_execute')
    @patch('os.path.exists')
    @requirements(['#0050', '#0051', '#0052'])
    def test_get_repo_root_path(self, mock_os_path, mock_git_execute):
        mock_os_path.return_value = True
        mock_git_execute.return_value = os.path.abspath(__file__)
        result = source.git_utils.get_repo_root(__file__)
        self.assertEqual(result, __file__)
