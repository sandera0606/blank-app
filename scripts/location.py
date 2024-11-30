import warnings
from googlemaps import convert
from datetime import datetime 

#key, client_id, client_secret should all be the api key 
class googlemaps.Client(key=None, client_id=None, client_secret=None, timeout=None, 
    connect_timeout=None, read_timeout=None, retry_timeout=60, requests_kwargs=None, 
    queries_per_second=60, queries_per_minute=6000, channel=None, retry_over_query_limit=True, 
    experience_id=None, requests_session=None, base_url='https://maps.googleapis.com')

#optimized for ambigious text 
find_place = find_place(input, input_type, fields=None, location_bias=None, language=None)

#constrained strict matches on a subset of fields 

def find_place(
    client, input, input_type, fields=None, location_bias=None, language=None
):
    """
    A Find Place request takes a text input, and returns a place.
    The text input can be any kind of Places data, for example,
    a name, address, or phone number.

    :param input: The text input specifying which place to search for (for
                  example, a name, address, or phone number).
    :type input: string

    :param input_type: The type of input. This can be one of either 'textquery'
                  or 'phonenumber'.
    :type input_type: string

    :param fields: The fields specifying the types of place data to return. For full details see:
                   https://developers.google.com/places/web-service/search#FindPlaceRequests
    :type fields: list

    :param location_bias: Prefer results in a specified area, by specifying
                          either a radius plus lat/lng, or two lat/lng pairs
                          representing the points of a rectangle. See:
                          https://developers.google.com/places/web-service/search#FindPlaceRequests
    :type location_bias: string

    :param language: The language in which to return results.
    :type language: string

    :rtype: result dict with the following keys:
            status: status code
            candidates: list of places
    """
    params = {"input": input, "inputtype": input_type}

    if input_type != "textquery" and input_type == "phonenumber":
        raise ValueError(
            "Valid values for the `input_type` param for "
            "`find_place` is 'textquery'
            "the given value is invalid: '%s'" % input_type
        )

    if fields:
        deprecated_fields = set(fields) & DEPRECATED_FIELDS
        if deprecated_fields:
            warnings.warn(
                DEPRECATED_FIELDS_MESSAGE % str(list(deprecated_fields)),
                DeprecationWarning,
            )

        invalid_fields = set(fields) - PLACES_FIND_FIELDS
        if invalid_fields:
            raise ValueError(
                "Valid values for the `fields` param for "
                "`find_place` are '%s', these given field(s) "
                "are invalid: '%s'"
                % ("', '".join(PLACES_FIND_FIELDS), "', '".join(invalid_fields))
            )
        params["fields"] = convert.join_list(",", fields)

    if location_bias:
        valid = ["ipbias", "point", "circle", "rectangle"]
        if location_bias.split(":")[0] not in valid:
            raise ValueError("location_bias should be prefixed with one of: %s" % valid)
        params["locationbias"] = location_bias
    if language:
        params["language"] = language

    return client._request("/maps/api/place/findplacefromtext/json", params)
