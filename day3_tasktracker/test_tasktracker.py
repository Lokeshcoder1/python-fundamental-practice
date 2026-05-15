from tasktracker import TaskTracker


def test_remove_from_empty_list():
    tt=TaskTracker()
    assert tt.remove_task(1) is False
def test_add_task():
    tt = TaskTracker()
    assert tt.add_task('Go to store','','high','2026-05-16') is True

def test_remove_from_existing_list():
    tt = TaskTracker()
    tt.add_task('Go tho market','','medium','2026-05-17')
    assert tt.remove_task(1) is True

def  test_mark_done_non_existing():
    tt = TaskTracker()
    assert tt.mark_done(4) is False

def  test_mark_done_existing():
    tt = TaskTracker()
    tt.add_task('Go tho market', '', 'medium', '2026-05-17')
    assert tt.mark_done(1) is True

def test_load_from_empty_file(tmp_path):
    tt = TaskTracker()
    test_file=tmp_path/ 'test.json'
    tt.load_from_file(test_file)

    assert tt.tasks == []

def test_save_to_file(tmp_path):
    tt = TaskTracker()
    test_file=tmp_path/'test.json'
    tt.add_task('Go tho market','','medium','2026-05-17')
    assert len(tt.tasks) ==1




