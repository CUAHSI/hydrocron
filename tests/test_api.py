"""
Tests for API queries
"""
import json


def test_timeseries_lambda_handler_geojson(hydrocron_api):
    """
    Test the lambda handler for the timeseries endpoint
    Parameters
    ----------
    hydrocron_api: Fixture ensuring the database is configured for the api
    """
    import hydrocron.api.controllers.timeseries

    event = {
        "body": {
            "feature": "Reach",
            "feature_id": "71224100223",
            "start_time": "2023-06-04T00:00:00Z",
            "end_time": "2023-06-23T00:00:00Z",
            "output": "geojson",
            "fields": "reach_id,time_str,wse,geometry"
        }
    }

    context = "_"
    result = hydrocron.api.controllers.timeseries.lambda_handler(event, context)
    print(result['results']['geojson'])
    assert result['status'] == '200 OK' and \
           result['results']['geojson'] == {'type': 'FeatureCollection', 'features': [
                    {'properties': {'reach_id': '71224100223', 'time_str': '2023-06-10T19:39:43Z',
                    'wse': '286.2983'}, 'geometry': {'coordinates':
                    [[-95.564991, 50.223686], [-95.564559, 50.223479],
                    [-95.564133, 50.223381],
                    [-95.563713, 50.22339], [-95.563296, 50.223453],
                    [-95.562884, 50.223624],
                    [-95.562473, 50.223795], [-95.562062, 50.223966],
                    [-95.56165, 50.224137],
                    [-95.561242, 50.224362], [-95.560917, 50.224585],
                    [-95.560595, 50.224862],
                    [-95.560271, 50.225085], [-95.559946, 50.225308],
                    [-95.559946, 50.225308],
                    [-95.559213, 50.225756], [-95.558804, 50.225981],
                    [-95.558567, 50.226256],
                    [-95.558413, 50.226529], [-95.558343, 50.226801],
                    [-95.558274, 50.227072],
                    [-95.558288, 50.227342], [-95.558303, 50.227611],
                    [-95.558317, 50.227881],
                    [-95.558416, 50.228148], [-95.558514, 50.228416],
                    [-95.558697, 50.228682],
                    [-95.558795, 50.22895], [-95.558978, 50.229216],
                    [-95.559076, 50.229483],
                    [-95.559259, 50.229749], [-95.559357, 50.230017],
                    [-95.559455, 50.230284],
                    [-95.55947, 50.230554], [-95.559484, 50.230823],
                    [-95.559583, 50.231091],
                    [-95.559765, 50.231357], [-95.559864, 50.231625],
                    [-95.559878, 50.231894],
                    [-95.559809, 50.232166], [-95.559571, 50.232441],
                    [-95.559165, 50.23272],
                    [-95.558757, 50.232944], [-95.558348, 50.233169],
                    [-95.557939, 50.233394],
                    [-95.55753, 50.233619], [-95.557206, 50.233842],
                    [-95.556884, 50.234119],
                    [-95.556562, 50.234396], [-95.556241, 50.234673],
                    [-95.556003, 50.234948],
                    [-95.555681, 50.235225], [-95.555443, 50.2355],
                    [-95.555206, 50.235775],
                    [-95.555136, 50.236047], [-95.555066, 50.236318],
                    [-95.555081, 50.236588],
                    [-95.555011, 50.236859], [-95.554941, 50.23713],
                    [-95.554701, 50.237351],
                    [-95.554376, 50.237575], [-95.554052, 50.237798],
                    [-95.553727, 50.238021],
                    [-95.553727, 50.238021], [-95.55308, 50.238521],
                    [-95.552843, 50.238796],
                    [-95.552521, 50.239073], [-95.552367, 50.239346],
                    [-95.552297, 50.239617],
                    [-95.552312, 50.239887], [-95.552326, 50.240156],
                    [-95.552425, 50.240424],
                    [-95.552439, 50.240693], [-95.552453, 50.240963],
                    [-95.552468, 50.241233],
                    [-95.552482, 50.241502], [-95.552497, 50.241772],
                    [-95.552511, 50.242041],
                    [-95.552525, 50.242311], [-95.552456, 50.242582],
                    [-95.552299, 50.242801],
                    [-95.552056, 50.242969], [-95.551728, 50.243138],
                    [-95.551314, 50.243255],
                    [-95.550899, 50.243372], [-95.550487, 50.243543],
                    [-95.550076, 50.243714],
                    [-95.549661, 50.243831], [-95.549249, 50.244002],
                    [-95.548838, 50.244173],
                    [-95.548423, 50.24429], [-95.548011, 50.244461],
                    [-95.547603, 50.244686],
                    [-95.547278, 50.244909], [-95.546953, 50.245132],
                    [-95.546715, 50.245407],
                    [-95.546561, 50.24568], [-95.546492, 50.245951],
                    [-95.546422, 50.246223],
                    [-95.546436, 50.246492], [-95.546367, 50.246764],
                    [-95.546297, 50.247035],
                    [-95.546143, 50.247308], [-95.54599, 50.247582],
                    [-95.545752, 50.247857],
                    [-95.545598, 50.24813], [-95.545444, 50.248403],
                    [-95.545374, 50.248674],
                    [-95.545305, 50.248946], [-95.545319, 50.249215],
                    [-95.545333, 50.249485],
                    [-95.545348, 50.249754], [-95.545446, 50.250022],
                    [-95.545545, 50.25029],
                    [-95.545727, 50.250556], [-95.54591, 50.250822],
                    [-95.546176, 50.251086],
                    [-95.546359, 50.251351], [-95.546625, 50.251615],
                    [-95.546892, 50.251879],
                    [-95.547075, 50.252145], [-95.547257, 50.252411],
                    [-95.54744, 50.252677],
                    [-95.547538, 50.252945], [-95.547553, 50.253214],
                    [-95.547651, 50.253482],
                    [-95.547581, 50.253753], [-95.547512, 50.254025],
                    [-95.547442, 50.254296],
                    [-95.547372, 50.254568], [-95.547303, 50.254839],
                    [-95.547317, 50.255108],
                    [-95.547247, 50.25538], [-95.547177, 50.255651],
                    [-95.547192, 50.255921],
                    [-95.547206, 50.25619], [-95.547221, 50.25646],
                    [-95.547319, 50.256728],
                    [-95.547418, 50.256995], [-95.547432, 50.257265],
                    [-95.547446, 50.257534],
                    [-95.547461, 50.257804], [-95.547475, 50.258073],
                    [-95.547489, 50.258343],
                    [-95.547504, 50.258613], [-95.547518, 50.258882],
                    [-95.547449, 50.259153],
                    [-95.547379, 50.259425], [-95.547309, 50.259696],
                    [-95.547239, 50.259968],
                    [-95.547086, 50.260241], [-95.547016, 50.260512],
                    [-95.546946, 50.260784],
                    [-95.546876, 50.261055], [-95.546807, 50.261326],
                    [-95.546737, 50.261598],
                    [-95.546583, 50.261871], [-95.546345, 50.262146],
                    [-95.54602, 50.262369],
                    [-95.545611, 50.262594], [-95.5452, 50.262765],
                    [-95.544788, 50.262936],
                    [-95.544373, 50.263053], [-95.543961, 50.263224],
                    [-95.543546, 50.263341],
                    [-95.543135, 50.263512], [-95.542723, 50.263683],
                    [-95.542314, 50.263907],
                    [-95.541989, 50.26413], [-95.541667, 50.264407],
                    [-95.541345, 50.264684],
                    [-95.541107, 50.264959], [-95.540869, 50.265234],
                    [-95.540631, 50.265509],
                    [-95.540393, 50.265785], [-95.540155, 50.26606],
                    [-95.539917, 50.266335],
                    [-95.539679, 50.26661], [-95.539441, 50.266885],
                    [-95.539203, 50.26716],
                    [-95.538962, 50.267381], [-95.538634, 50.26755],
                    [-95.538304, 50.267665],
                    [-95.537889, 50.267782], [-95.537471, 50.267845],
                    [-95.537056, 50.267962],
                    [-95.536642, 50.268079], [-95.536227, 50.268196],
                    [-95.535809, 50.268259],
                    [-95.535391, 50.268323], [-95.534974, 50.268386],
                    [-95.534556, 50.268449],
                    [-95.534138, 50.268512], [-95.533718, 50.268521],
                    [-95.5333, 50.268584],
                    [-95.532882, 50.268647], [-95.532552, 50.268762],
                    [-95.532224, 50.268931],
                    [-95.531986, 50.269206], [-95.531748, 50.269481],
                    [-95.531594, 50.269755],
                    [-95.531356, 50.27003], [-95.531202, 50.270303],
                    [-95.531048, 50.270576],
                    [-95.530978, 50.270847], [-95.530908, 50.271119],
                    [-95.530923, 50.271388],
                    [-95.530937, 50.271658], [-95.530951, 50.271927],
                    [-95.53105, 50.272195],
                    [-95.531148, 50.272463], [-95.531331, 50.272729],
                    [-95.531513, 50.272995],
                    [-95.531696, 50.273261], [-95.531878, 50.273526],
                    [-95.532145, 50.27379],
                    [-95.532327, 50.274056], [-95.532594, 50.27432],
                    [-95.532861, 50.274584],
                    [-95.533043, 50.27485], [-95.533142, 50.275118],
                    [-95.53324, 50.275386],
                    [-95.533339, 50.275653], [-95.533437, 50.275921],
                    [-95.533536, 50.276189],
                    [-95.533634, 50.276457], [-95.533732, 50.276724],
                    [-95.533747, 50.276994],
                    [-95.533761, 50.277263], [-95.533859, 50.277531],
                    [-95.533958, 50.277799],
                    [-95.53414, 50.278065], [-95.534323, 50.278331],
                    [-95.534506, 50.278596],
                    [-95.534688, 50.278862], [-95.534871, 50.279128],
                    [-95.534969, 50.279396],
                    [-95.535152, 50.279662], [-95.535334, 50.279928],
                    [-95.535433, 50.280195],
                    [-95.535615, 50.280461], [-95.535798, 50.280727],
                    [-95.535812, 50.280997],
                    [-95.535743, 50.281268], [-95.535589, 50.281541],
                    [-95.535266, 50.281818],
                    [-95.53486, 50.282097], [-95.534454, 50.282376],
                    [-95.534132, 50.282652],
                    [-95.533893, 50.282927], [-95.533824, 50.283199],
                    [-95.533838, 50.283468],
                    [-95.534021, 50.283734], [-95.534203, 50.284],
                    [-95.53447, 50.284264],
                    [-95.534652, 50.28453], [-95.534835, 50.284796],
                    [-95.535018, 50.285062],
                    [-95.5352, 50.285328], [-95.535383, 50.285594],
                    [-95.535565, 50.285859],
                    [-95.535832, 50.286123], [-95.536099, 50.286387],
                    [-95.53645, 50.28665],
                    [-95.536801, 50.286912], [-95.537152, 50.287174],
                    [-95.537418, 50.287438],
                    [-95.537601, 50.287704], [-95.5377, 50.287972],
                    [-95.537798, 50.288239],
                    [-95.537897, 50.288507], [-95.537995, 50.288775],
                    [-95.538093, 50.289043],
                    [-95.538192, 50.28931], [-95.538206, 50.28958],
                    [-95.538221, 50.289849],
                    [-95.538235, 50.290119], [-95.538334, 50.290387],
                    [-95.538432, 50.290654],
                    [-95.538531, 50.290922], [-95.538629, 50.29119]],
                    'type': 'LineString'}, 'type': 'Feature'}]}


def test_timeseries_lambda_handler_csv(hydrocron_api):
    """
    Test the lambda handler for the timeseries endpoint
    Parameters
    ----------
    hydrocron_api: Fixture ensuring the database is configured for the api
    """

    import hydrocron.api.controllers.timeseries

    event = {
        "body": {
            "feature": "Reach",
            "feature_id": "71224100223",
            "start_time": "2023-06-04T00:00:00Z",
            "end_time": "2023-06-23T00:00:00Z",
            "output": "csv",
            "fields": "reach_id,time_str,wse,geometry"
        }
    }

    context = "_"
    result = hydrocron.api.controllers.timeseries.lambda_handler(event, context)
    assert result['status'] == '200 OK'
    assert result['results']['csv'] == ('reach_id,time_str,wse,geometry\n' \
                                        '71224100223,2023-06-10T19:39:43Z,286.2983,LINESTRING (-95.564991 50.223686, ' \
                                        '-95.564559 50.223479, -95.564133 50.223381, -95.563713 50.22339, -95.563296 ' \
                                        '50.223453, -95.562884 50.223624, -95.562473 50.223795, -95.562062 50.223966, ' \
                                        '-95.56165 50.224137, -95.561242 50.224362, -95.560917 50.224585, -95.560595 ' \
                                        '50.224862, -95.560271 50.225085, -95.559946 50.225308, -95.559946 50.225308, ' \
                                        '-95.559213 50.225756, -95.558804 50.225981, -95.558567 50.226256, -95.558413 ' \
                                        '50.226529, -95.558343 50.226801, -95.558274 50.227072, -95.558288 50.227342, ' \
                                        '-95.558303 50.227611, -95.558317 50.227881, -95.558416 50.228148, -95.558514 ' \
                                        '50.228416, -95.558697 50.228682, -95.558795 50.22895, -95.558978 50.229216, ' \
                                        '-95.559076 50.229483, -95.559259 50.229749, -95.559357 50.230017, -95.559455 ' \
                                        '50.230284, -95.55947 50.230554, -95.559484 50.230823, -95.559583 50.231091, ' \
                                        '-95.559765 50.231357, -95.559864 50.231625, -95.559878 50.231894, -95.559809 ' \
                                        '50.232166, -95.559571 50.232441, -95.559165 50.23272, -95.558757 50.232944, ' \
                                        '-95.558348 50.233169, -95.557939 50.233394, -95.55753 50.233619, -95.557206 ' \
                                        '50.233842, -95.556884 50.234119, -95.556562 50.234396, -95.556241 50.234673, ' \
                                        '-95.556003 50.234948, -95.555681 50.235225, -95.555443 50.2355, -95.555206 ' \
                                        '50.235775, -95.555136 50.236047, -95.555066 50.236318, -95.555081 50.236588, ' \
                                        '-95.555011 50.236859, -95.554941 50.23713, -95.554701 50.237351, -95.554376 ' \
                                        '50.237575, -95.554052 50.237798, -95.553727 50.238021, -95.553727 50.238021, ' \
                                        '-95.55308 50.238521, -95.552843 50.238796, -95.552521 50.239073, -95.552367 ' \
                                        '50.239346, -95.552297 50.239617, -95.552312 50.239887, -95.552326 50.240156, ' \
                                        '-95.552425 50.240424, -95.552439 50.240693, -95.552453 50.240963, -95.552468 ' \
                                        '50.241233, -95.552482 50.241502, -95.552497 50.241772, -95.552511 50.242041, ' \
                                        '-95.552525 50.242311, -95.552456 50.242582, -95.552299 50.242801, -95.552056 ' \
                                        '50.242969, -95.551728 50.243138, -95.551314 50.243255, -95.550899 50.243372, ' \
                                        '-95.550487 50.243543, -95.550076 50.243714, -95.549661 50.243831, -95.549249 ' \
                                        '50.244002, -95.548838 50.244173, -95.548423 50.24429, -95.548011 50.244461, ' \
                                        '-95.547603 50.244686, -95.547278 50.244909, -95.546953 50.245132, -95.546715 ' \
                                        '50.245407, -95.546561 50.24568, -95.546492 50.245951, -95.546422 50.246223, ' \
                                        '-95.546436 50.246492, -95.546367 50.246764, -95.546297 50.247035, -95.546143 ' \
                                        '50.247308, -95.54599 50.247582, -95.545752 50.247857, -95.545598 50.24813, ' \
                                        '-95.545444 50.248403, -95.545374 50.248674, -95.545305 50.248946, -95.545319 ' \
                                        '50.249215, -95.545333 50.249485, -95.545348 50.249754, -95.545446 50.250022, ' \
                                        '-95.545545 50.25029, -95.545727 50.250556, -95.54591 50.250822, -95.546176 ' \
                                        '50.251086, -95.546359 50.251351, -95.546625 50.251615, -95.546892 50.251879, ' \
                                        '-95.547075 50.252145, -95.547257 50.252411, -95.54744 50.252677, -95.547538 ' \
                                        '50.252945, -95.547553 50.253214, -95.547651 50.253482, -95.547581 50.253753, ' \
                                        '-95.547512 50.254025, -95.547442 50.254296, -95.547372 50.254568, -95.547303 ' \
                                        '50.254839, -95.547317 50.255108, -95.547247 50.25538, -95.547177 50.255651, ' \
                                        '-95.547192 50.255921, -95.547206 50.25619, -95.547221 50.25646, -95.547319 ' \
                                        '50.256728, -95.547418 50.256995, -95.547432 50.257265, -95.547446 50.257534, ' \
                                        '-95.547461 50.257804, -95.547475 50.258073, -95.547489 50.258343, -95.547504 ' \
                                        '50.258613, -95.547518 50.258882, -95.547449 50.259153, -95.547379 50.259425, ' \
                                        '-95.547309 50.259696, -95.547239 50.259968, -95.547086 50.260241, -95.547016 ' \
                                        '50.260512, -95.546946 50.260784, -95.546876 50.261055, -95.546807 50.261326, ' \
                                        '-95.546737 50.261598, -95.546583 50.261871, -95.546345 50.262146, -95.54602 ' \
                                        '50.262369, -95.545611 50.262594, -95.5452 50.262765, -95.544788 50.262936, ' \
                                        '-95.544373 50.263053, -95.543961 50.263224, -95.543546 50.263341, -95.543135 ' \
                                        '50.263512, -95.542723 50.263683, -95.542314 50.263907, -95.541989 50.26413, ' \
                                        '-95.541667 50.264407, -95.541345 50.264684, -95.541107 50.264959, -95.540869 ' \
                                        '50.265234, -95.540631 50.265509, -95.540393 50.265785, -95.540155 50.26606, ' \
                                        '-95.539917 50.266335, -95.539679 50.26661, -95.539441 50.266885, -95.539203 ' \
                                        '50.26716, -95.538962 50.267381, -95.538634 50.26755, -95.538304 50.267665, ' \
                                        '-95.537889 50.267782, -95.537471 50.267845, -95.537056 50.267962, -95.536642 ' \
                                        '50.268079, -95.536227 50.268196, -95.535809 50.268259, -95.535391 50.268323, ' \
                                        '-95.534974 50.268386, -95.534556 50.268449, -95.534138 50.268512, -95.533718 ' \
                                        '50.268521, -95.5333 50.268584, -95.532882 50.268647, -95.532552 50.268762, ' \
                                        '-95.532224 50.268931, -95.531986 50.269206, -95.531748 50.269481, -95.531594 ' \
                                        '50.269755, -95.531356 50.27003, -95.531202 50.270303, -95.531048 50.270576, ' \
                                        '-95.530978 50.270847, -95.530908 50.271119, -95.530923 50.271388, -95.530937 ' \
                                        '50.271658, -95.530951 50.271927, -95.53105 50.272195, -95.531148 50.272463, ' \
                                        '-95.531331 50.272729, -95.531513 50.272995, -95.531696 50.273261, -95.531878 ' \
                                        '50.273526, -95.532145 50.27379, -95.532327 50.274056, -95.532594 50.27432, ' \
                                        '-95.532861 50.274584, -95.533043 50.27485, -95.533142 50.275118, -95.53324 ' \
                                        '50.275386, -95.533339 50.275653, -95.533437 50.275921, -95.533536 50.276189, ' \
                                        '-95.533634 50.276457, -95.533732 50.276724, -95.533747 50.276994, -95.533761 ' \
                                        '50.277263, -95.533859 50.277531, -95.533958 50.277799, -95.53414 50.278065, ' \
                                        '-95.534323 50.278331, -95.534506 50.278596, -95.534688 50.278862, -95.534871 ' \
                                        '50.279128, -95.534969 50.279396, -95.535152 50.279662, -95.535334 50.279928, ' \
                                        '-95.535433 50.280195, -95.535615 50.280461, -95.535798 50.280727, -95.535812 ' \
                                        '50.280997, -95.535743 50.281268, -95.535589 50.281541, -95.535266 50.281818, ' \
                                        '-95.53486 50.282097, -95.534454 50.282376, -95.534132 50.282652, -95.533893 ' \
                                        '50.282927, -95.533824 50.283199, -95.533838 50.283468, -95.534021 50.283734, ' \
                                        '-95.534203 50.284, -95.53447 50.284264, -95.534652 50.28453, -95.534835 ' \
                                        '50.284796, -95.535018 50.285062, -95.5352 50.285328, -95.535383 50.285594, ' \
                                        '-95.535565 50.285859, -95.535832 50.286123, -95.536099 50.286387, -95.53645 ' \
                                        '50.28665, -95.536801 50.286912, -95.537152 50.287174, -95.537418 50.287438, ' \
                                        '-95.537601 50.287704, -95.5377 50.287972, -95.537798 50.288239, -95.537897 ' \
                                        '50.288507, -95.537995 50.288775, -95.538093 50.289043, -95.538192 50.28931, ' \
                                        '-95.538206 50.28958, -95.538221 50.289849, -95.538235 50.290119, -95.538334 ' \
                                        '50.290387, -95.538432 50.290654, -95.538531 50.290922, -95.538629 ' \
                                        '50.29119),\n')
