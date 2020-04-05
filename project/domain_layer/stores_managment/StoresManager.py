from project.domain_layer.stores_managment.Product import Product
from project.domain_layer.stores_managment.Store import Store
from project.domain_layer.users_managment import User


class StoresManager:
    def __init__(self):
        self.stores = {int: Store}
        self.stores_idx = 0

    def search(self, search_term: str = "", categories: [str] = None, key_words: [str] = None) -> {Store: [Product]}:
        """

        Args:
            search_term: part of the wanted product name
            categories: categories to search in
            key_words:

        Returns:dist {Store:list of products in store}

        """
        search_result = {}
        for store_id in self.stores.keys():
            search_in_store = self.stores.get(store_id).search(search_term, categories, key_words)
            if search_in_store is not None:
                search_result[self.stores.get(store_id)] = search_in_store
        return search_result

    def get_store(self, store_id: int) -> Store:
        if store_id in self.stores.keys():
            return self.stores.get(store_id)
        else:
            raise ValueError("wrong store id", store_id)

    def add_product_to_store(self, store_id: int, user: User, product_name: str, product_price: int,
                             product_categories: [str],
                             key_words: [str]) -> bool:
        """

        Args:
            store_id:
            user:
            product_name:
            product_price:
            product_categories:
            key_words:

        Returns:

        """
        return self.stores.get(store_id).add_product(user, product_name, product_price, product_categories, key_words)

    def appoint_manager_to_store(self, store_id, owner, to_appoint):
        """

        Args:
            store_id:
            owner:
            to_appoint:
        """
        self.stores.get(store_id).appoint_manager(owner, to_appoint)

    def appoint_owner_to_store(self, store_id, owner, to_appoint):
        """

        Args:
            store_id:
            owner:
            to_appoint:
        """
        self.stores.get(store_id).appoint_owner(owner, to_appoint)

    def add_permission_to_manager_in_store(self, store_id, owner, manager, permission: str):
        self.stores.get(store_id).add_permission_to_manager(owner, manager, permission)

    def remove_permission_from_manager_in_store(self, store_id, owner, manager, permission: str):
        self.stores.get(store_id).remove_permission_from_manager(owner, manager, permission)