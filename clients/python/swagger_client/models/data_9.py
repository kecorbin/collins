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


class Data9(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cardimageurl=None, dockerimage=None, company=None, description=None):
        """
        Data9 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cardimageurl': 'str',
            'dockerimage': 'str',
            'company': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'cardimageurl': 'cardimageurl',
            'dockerimage': 'dockerimage',
            'company': 'company',
            'description': 'description'
        }

        self._cardimageurl = cardimageurl
        self._dockerimage = dockerimage
        self._company = company
        self._description = description

    @property
    def cardimageurl(self):
        """
        Gets the cardimageurl of this Data9.
        

        :return: The cardimageurl of this Data9.
        :rtype: str
        """
        return self._cardimageurl

    @cardimageurl.setter
    def cardimageurl(self, cardimageurl):
        """
        Sets the cardimageurl of this Data9.
        

        :param cardimageurl: The cardimageurl of this Data9.
        :type: str
        """
        if cardimageurl is None:
            raise ValueError("Invalid value for `cardimageurl`, must not be `None`")

        self._cardimageurl = cardimageurl

    @property
    def dockerimage(self):
        """
        Gets the dockerimage of this Data9.
        

        :return: The dockerimage of this Data9.
        :rtype: str
        """
        return self._dockerimage

    @dockerimage.setter
    def dockerimage(self, dockerimage):
        """
        Sets the dockerimage of this Data9.
        

        :param dockerimage: The dockerimage of this Data9.
        :type: str
        """
        if dockerimage is None:
            raise ValueError("Invalid value for `dockerimage`, must not be `None`")

        self._dockerimage = dockerimage

    @property
    def company(self):
        """
        Gets the company of this Data9.
        

        :return: The company of this Data9.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this Data9.
        

        :param company: The company of this Data9.
        :type: str
        """
        if company is None:
            raise ValueError("Invalid value for `company`, must not be `None`")

        self._company = company

    @property
    def description(self):
        """
        Gets the description of this Data9.
        

        :return: The description of this Data9.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Data9.
        

        :param description: The description of this Data9.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

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
        if not isinstance(other, Data9):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other