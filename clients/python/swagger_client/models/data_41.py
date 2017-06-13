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


class Data41(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, status=None, mfg=None, ip=None, firmware=None, note=None, dev_name=None, uniqueid=None, model=None):
        """
        Data41 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'str',
            'mfg': 'str',
            'ip': 'str',
            'firmware': 'str',
            'note': 'str',
            'dev_name': 'str',
            'uniqueid': 'str',
            'model': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'mfg': 'mfg',
            'ip': 'ip',
            'firmware': 'firmware',
            'note': 'note',
            'dev_name': 'dev_name',
            'uniqueid': 'uniqueid',
            'model': 'model'
        }

        self._status = status
        self._mfg = mfg
        self._ip = ip
        self._firmware = firmware
        self._note = note
        self._dev_name = dev_name
        self._uniqueid = uniqueid
        self._model = model

    @property
    def status(self):
        """
        Gets the status of this Data41.
        

        :return: The status of this Data41.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Data41.
        

        :param status: The status of this Data41.
        :type: str
        """

        self._status = status

    @property
    def mfg(self):
        """
        Gets the mfg of this Data41.
        

        :return: The mfg of this Data41.
        :rtype: str
        """
        return self._mfg

    @mfg.setter
    def mfg(self, mfg):
        """
        Sets the mfg of this Data41.
        

        :param mfg: The mfg of this Data41.
        :type: str
        """

        self._mfg = mfg

    @property
    def ip(self):
        """
        Gets the ip of this Data41.
        

        :return: The ip of this Data41.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this Data41.
        

        :param ip: The ip of this Data41.
        :type: str
        """

        self._ip = ip

    @property
    def firmware(self):
        """
        Gets the firmware of this Data41.
        

        :return: The firmware of this Data41.
        :rtype: str
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """
        Sets the firmware of this Data41.
        

        :param firmware: The firmware of this Data41.
        :type: str
        """

        self._firmware = firmware

    @property
    def note(self):
        """
        Gets the note of this Data41.
        

        :return: The note of this Data41.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this Data41.
        

        :param note: The note of this Data41.
        :type: str
        """

        self._note = note

    @property
    def dev_name(self):
        """
        Gets the dev_name of this Data41.
        

        :return: The dev_name of this Data41.
        :rtype: str
        """
        return self._dev_name

    @dev_name.setter
    def dev_name(self, dev_name):
        """
        Sets the dev_name of this Data41.
        

        :param dev_name: The dev_name of this Data41.
        :type: str
        """

        self._dev_name = dev_name

    @property
    def uniqueid(self):
        """
        Gets the uniqueid of this Data41.
        

        :return: The uniqueid of this Data41.
        :rtype: str
        """
        return self._uniqueid

    @uniqueid.setter
    def uniqueid(self, uniqueid):
        """
        Sets the uniqueid of this Data41.
        

        :param uniqueid: The uniqueid of this Data41.
        :type: str
        """

        self._uniqueid = uniqueid

    @property
    def model(self):
        """
        Gets the model of this Data41.
        

        :return: The model of this Data41.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this Data41.
        

        :param model: The model of this Data41.
        :type: str
        """

        self._model = model

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
        if not isinstance(other, Data41):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other