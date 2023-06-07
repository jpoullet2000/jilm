from jilm.document_loader import DocumentLoader

def test_load_single_document(csv_file):
    csv_args = {"delimiter": ","}
    res = DocumentLoader.load_single_document(csv_file, csv_args=csv_args)
    assert res is not None
    assert res.page_content == 'mpg: 18.0\ncylinders: 8.0\ndisplacement: 307.0\nhorsepower: 130.0\nweight: 3504.0\nacceleration: 12.0\nmodel_year: 70.0\norigin: 1.0\ncar_name: chevrolet chevelle malibu'

def test_load_documents(data_folder):
    res = DocumentLoader.load_documents(data_folder)
    assert res is not None
    assert len(res) > 1
    assert res[0].page_content == 'mpg: 18.0\ncylinders: 8.0\ndisplacement: 307.0\nhorsepower: 130.0\nweight: 3504.0\nacceleration: 12.0\nmodel_year: 70.0\norigin: 1.0\ncar_name: chevrolet chevelle malibu'
