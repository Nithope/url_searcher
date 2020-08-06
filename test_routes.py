import requests,os

base_url=os.getenv('BASE_URL')

def test_post_list_db():
    # base_url="http://localhost:9099/"
    post_url = 'list_db'

    response = requests.post(url=base_url+"".join(post_url))
    assert "Empty" in response.json()

def test_post_url():
    # base_url="http://localhost:9099/"
    post_url = 'url'
    URL = "https://github.com/nithope"

    response = requests.post(url=base_url+"".join(post_url),data={
        'url': URL
    })
    assert "URL ADDED TO DB" in response.json()

def test_post_list_db2():
    # base_url="http://localhost:9099/"
    post_url = 'list_db'
    URL = "https://github.com/nithope"

    response = requests.post(url=base_url+"".join(post_url))
    assert URL in response.json()

def test_post_inception_url():
    # base_url="http://localhost:9099/"
    post_url = 'inception_url'

    response = requests.post(url=base_url+"".join(post_url))
    assert "All this info were added in the db" in response.json()

def test_post_list_db3():
    # base_url="http://localhost:9099/"
    post_url = 'list_db'
    URL = "https://github.blog/2020-08-05-github-actions-enterprise-runners-and-fine-grained-access-settings-with-runner-groups/"

    response = requests.post(url=base_url+"".join(post_url))
    assert URL in response.json()


def test_post_drop_col():
    # base_url="http://localhost:9099/"
    post_url = 'drop_col'

    response = requests.post(url=base_url+"".join(post_url))
    assert "Dropped" in response.json()

def test_post_list_db4():
    # base_url="http://localhost:9099/"
    post_url = 'list_db'

    response = requests.post(url=base_url+"".join(post_url))
    assert "Empty" in response.json()

