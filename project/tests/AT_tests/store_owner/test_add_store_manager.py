import unittest

from project.tests.AT_tests.test_env.Driver import Driver
import jsonpickle

class test_addStoremanager(unittest.TestCase):
    def setUp(self) -> None:
        self.service = Driver.make_bridge()
        self.service.register("new manager", "new pass")
        self.service.register("owner", "pass")
        self.service.login("owner", "pass")
        self.store_id = self.service.Open_store("my store")


    def test_add_new_manager_success(self):
        self.service.add_new_store_manager("new manager", self.store_id)
        self.service.logout()
        self.service.login("new manager", "new pass")
        maneged_stores = jsonpickle.decode(self.service.get_managed_stores())
        x=5
        self.assertIn(str(self.store_id), maneged_stores)

    def test_add_new_manager_sad(self):
        self.assertFalse(self.service.add_new_store_manager("not new manager", self.store_id))
        self.test_add_new_manager_success()
        self.service.logout()
        self.service.login("owner", "pass")
        self.assertFalse(self.service.add_new_store_manager("new manager", self.store_id))

    def test_add_new_manager_bad(self):
        self.assertFalse(self.service.add_new_store_manager("not new manager", self.store_id+40))


if __name__ == '__main__':
    unittest.main()
