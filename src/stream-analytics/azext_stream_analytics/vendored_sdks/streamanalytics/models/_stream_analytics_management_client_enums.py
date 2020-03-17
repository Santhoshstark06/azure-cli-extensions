# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class SkuName(str, Enum):

    standard = "Standard"


class OutputStartMode(str, Enum):

    job_start_time = "JobStartTime"
    custom_time = "CustomTime"
    last_output_event_time = "LastOutputEventTime"


class EventsOutOfOrderPolicy(str, Enum):

    adjust = "Adjust"
    drop = "Drop"


class OutputErrorPolicy(str, Enum):

    stop = "Stop"
    drop = "Drop"


class CompatibilityLevel(str, Enum):

    one_full_stop_zero = "1.0"


class JsonOutputSerializationFormat(str, Enum):

    line_separated = "LineSeparated"
    array = "Array"


class Encoding(str, Enum):

    utf8 = "UTF8"


class UdfType(str, Enum):

    scalar = "Scalar"