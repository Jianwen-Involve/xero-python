# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Benefit(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "id": "str",
        "name": "str",
        "category": "str",
        "liability_account_id": "str",
        "expense_account_id": "str",
        "calculation_type_nz": "str",
        "standard_amount": "float",
        "percentage": "float",
        "company_max": "float",
        "current_record": "bool",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "category": "category",
        "liability_account_id": "liabilityAccountId",
        "expense_account_id": "expenseAccountId",
        "calculation_type_nz": "calculationTypeNZ",
        "standard_amount": "standardAmount",
        "percentage": "percentage",
        "company_max": "companyMax",
        "current_record": "currentRecord",
    }

    def __init__(
        self,
        id=None,
        name=None,
        category=None,
        liability_account_id=None,
        expense_account_id=None,
        calculation_type_nz=None,
        standard_amount=None,
        percentage=None,
        company_max=None,
        current_record=None,
    ):  # noqa: E501
        """Benefit - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._category = None
        self._liability_account_id = None
        self._expense_account_id = None
        self._calculation_type_nz = None
        self._standard_amount = None
        self._percentage = None
        self._company_max = None
        self._current_record = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.category = category
        self.liability_account_id = liability_account_id
        self.expense_account_id = expense_account_id
        if calculation_type_nz is not None:
            self.calculation_type_nz = calculation_type_nz
        if standard_amount is not None:
            self.standard_amount = standard_amount
        if percentage is not None:
            self.percentage = percentage
        if company_max is not None:
            self.company_max = company_max
        if current_record is not None:
            self.current_record = current_record

    @property
    def id(self):
        """Gets the id of this Benefit.  # noqa: E501

        The Xero identifier for superannuation  # noqa: E501

        :return: The id of this Benefit.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Benefit.

        The Xero identifier for superannuation  # noqa: E501

        :param id: The id of this Benefit.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Benefit.  # noqa: E501

        Name of the superannuations  # noqa: E501

        :return: The name of this Benefit.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Benefit.

        Name of the superannuations  # noqa: E501

        :param name: The name of this Benefit.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def category(self):
        """Gets the category of this Benefit.  # noqa: E501

        Superannuations Category type  # noqa: E501

        :return: The category of this Benefit.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Benefit.

        Superannuations Category type  # noqa: E501

        :param category: The category of this Benefit.  # noqa: E501
        :type: str
        """
        if category is None:
            raise ValueError(
                "Invalid value for `category`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["KiwiSaver", "ComplyingFund", "Other", "None"]  # noqa: E501

        if category:
            if category not in allowed_values:
                raise ValueError(
                    "Invalid value for `category` ({0}), must be one of {1}".format(  # noqa: E501
                        category, allowed_values
                    )
                )

        self._category = category

    @property
    def liability_account_id(self):
        """Gets the liability_account_id of this Benefit.  # noqa: E501

        Xero identifier for Liability Account  # noqa: E501

        :return: The liability_account_id of this Benefit.  # noqa: E501
        :rtype: str
        """
        return self._liability_account_id

    @liability_account_id.setter
    def liability_account_id(self, liability_account_id):
        """Sets the liability_account_id of this Benefit.

        Xero identifier for Liability Account  # noqa: E501

        :param liability_account_id: The liability_account_id of this Benefit.  # noqa: E501
        :type: str
        """
        if liability_account_id is None:
            raise ValueError(
                "Invalid value for `liability_account_id`, must not be `None`"
            )  # noqa: E501

        self._liability_account_id = liability_account_id

    @property
    def expense_account_id(self):
        """Gets the expense_account_id of this Benefit.  # noqa: E501

        Xero identifier for Expense Account  # noqa: E501

        :return: The expense_account_id of this Benefit.  # noqa: E501
        :rtype: str
        """
        return self._expense_account_id

    @expense_account_id.setter
    def expense_account_id(self, expense_account_id):
        """Sets the expense_account_id of this Benefit.

        Xero identifier for Expense Account  # noqa: E501

        :param expense_account_id: The expense_account_id of this Benefit.  # noqa: E501
        :type: str
        """
        if expense_account_id is None:
            raise ValueError(
                "Invalid value for `expense_account_id`, must not be `None`"
            )  # noqa: E501

        self._expense_account_id = expense_account_id

    @property
    def calculation_type_nz(self):
        """Gets the calculation_type_nz of this Benefit.  # noqa: E501

        Calculation Type of the superannuation either FixedAmount or PercentageOfTaxableEarnings  # noqa: E501

        :return: The calculation_type_nz of this Benefit.  # noqa: E501
        :rtype: str
        """
        return self._calculation_type_nz

    @calculation_type_nz.setter
    def calculation_type_nz(self, calculation_type_nz):
        """Sets the calculation_type_nz of this Benefit.

        Calculation Type of the superannuation either FixedAmount or PercentageOfTaxableEarnings  # noqa: E501

        :param calculation_type_nz: The calculation_type_nz of this Benefit.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "FixedAmount",
            "PercentageOfTaxableEarnings",
            "None",
        ]  # noqa: E501

        if calculation_type_nz:
            if calculation_type_nz not in allowed_values:
                raise ValueError(
                    "Invalid value for `calculation_type_nz` ({0}), must be one of {1}".format(  # noqa: E501
                        calculation_type_nz, allowed_values
                    )
                )

        self._calculation_type_nz = calculation_type_nz

    @property
    def standard_amount(self):
        """Gets the standard_amount of this Benefit.  # noqa: E501

        Standard amount of the superannuation  # noqa: E501

        :return: The standard_amount of this Benefit.  # noqa: E501
        :rtype: float
        """
        return self._standard_amount

    @standard_amount.setter
    def standard_amount(self, standard_amount):
        """Sets the standard_amount of this Benefit.

        Standard amount of the superannuation  # noqa: E501

        :param standard_amount: The standard_amount of this Benefit.  # noqa: E501
        :type: float
        """

        self._standard_amount = standard_amount

    @property
    def percentage(self):
        """Gets the percentage of this Benefit.  # noqa: E501

        Percentage of Taxable Earnings of the superannuation  # noqa: E501

        :return: The percentage of this Benefit.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this Benefit.

        Percentage of Taxable Earnings of the superannuation  # noqa: E501

        :param percentage: The percentage of this Benefit.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def company_max(self):
        """Gets the company_max of this Benefit.  # noqa: E501

        Company Maximum amount of the superannuation  # noqa: E501

        :return: The company_max of this Benefit.  # noqa: E501
        :rtype: float
        """
        return self._company_max

    @company_max.setter
    def company_max(self, company_max):
        """Sets the company_max of this Benefit.

        Company Maximum amount of the superannuation  # noqa: E501

        :param company_max: The company_max of this Benefit.  # noqa: E501
        :type: float
        """

        self._company_max = company_max

    @property
    def current_record(self):
        """Gets the current_record of this Benefit.  # noqa: E501

        Identifier of a record is active or not.  # noqa: E501

        :return: The current_record of this Benefit.  # noqa: E501
        :rtype: bool
        """
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        """Sets the current_record of this Benefit.

        Identifier of a record is active or not.  # noqa: E501

        :param current_record: The current_record of this Benefit.  # noqa: E501
        :type: bool
        """

        self._current_record = current_record