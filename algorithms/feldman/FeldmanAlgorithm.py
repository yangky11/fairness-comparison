from BlackBoxAuditing.repairers.GeneralRepairer import Repairer
from pandas import DataFrame
from algorithms.Algorithm import Algorithm

REPAIR_LEVEL_DEFAULT = 1.0

class FeldmanAlgorithm(Algorithm):
    def __init__(self, algorithm):
        Algorithm.__init__(self)
        self.model = algorithm
        self.name = 'Feldman-' + self.model.get_name()
        print("WARNING: Feldman algorithm does not yet handle multiple sensitive attrs.")

    def run(self, train_df, test_df, class_attr, positive_class_val, sensitive_attrs, 
            single_sensitive, privileged_vals, params):
        if not 'lambda' in params:
            params = get_default_params()
        repair_level = params['lambda']

        ## TODO: check about multiple sensitive attrs
        repaired_train_df = self.repair(train_df, sensitive_attrs, repair_level)

        # What should be happening here is that the test_df is transformed using exactly the same
        # transformation as the train_df.  This will only be the case based on the usage below if
        # the distribution of each attribute conditioned on the sensitive attribute is the same
        # in the training set and the test set.
        repaired_test_df = self.repair(test_df, sensitive_attrs, repair_level) 

        return self.model.run(repaired_train_df, repaired_test_df, class_attr, positive_class_val,
                              sensitive_attrs, single_sensitive, privileged_vals, params)

    def get_param_info(self):
        """
        Returns lambda values in [0.0, 1.0] at increments of 0.05.
        """
        return { 'lambda' : [x/100.0 for x in range(0,105,5)] }

    def get_default_params(self):
        return { 'lambda' : REPAIR_LEVEL_DEFAULT }

    def repair(self, data_df, sensitive_attrs, repair_level):
        data = data_df.values.tolist()

        ## TODO: do something to make joint distribution over sensitive attrs
        index_to_repair = data_df.columns.get_loc(sensitive_attrs[0])
        headers = data_df.columns.tolist()
        repairer = Repairer(data, index_to_repair, repair_level, False)

        # The repaired data no longer includes its headers. 
        data = repairer.repair(data)
        data_df = DataFrame(data, columns = headers)
        return data_df

    def numerical_data_only(self):
        """
        The Feldman algorithm can preprocess both numerical and categorical data, the limiting
        factor is the capacity of the model that data is then passed to.
        """
        return self.model.numerical_data_only() 
