# coding: utf-8

"""
      Welcome to the interative api documentation   Have a look around...  

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Data5(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, every=None, period=None):
        """
        Data5 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'every': 'int',
            'period': 'str'
        }

        self.attribute_map = {
            'every': 'every',
            'period': 'period'
        }

        self._every = every
        self._period = period

    @property
    def every(self):
        """
        Gets the every of this Data5.
        

        :return: The every of this Data5.
        :rtype: int
        """
        return self._every

    @every.setter
    def every(self, every):
        """
        Sets the every of this Data5.
        

        :param every: The every of this Data5.
        :type: int
        """

        self._every = every

    @property
    def period(self):
        """
        Gets the period of this Data5.
        

        :return: The period of this Data5.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this Data5.
        

        :param period: The period of this Data5.
        :type: str
        """

        self._period = period

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Data5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
