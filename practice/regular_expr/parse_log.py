import requests
import re


def parse_graylog():
    p = re.compile(".*All instances in ASG passed (.*)-ELB health check \(Loop: ([1-9]{0,2})\).*$")
    loop_count_query = "http://localhost:12900/search/universal/relative?query=role%3Adfairy_worker%20AND" \
                       "%20application%3Adfairy%20AND%20message%3A%22All%20instances%20in%20ASG%20passed%22&range=166400" \
                       "&limit=150&fields=message "

    response = requests.get(loop_count_query, auth=('api', 'api123'))
    success_loops_each_roles = []
    for each in response.content.split("\n"):
        m = p.match(each)
        if m:
            success_loops_each_roles.append({'role': m.group(1), 'success_loop_count': int(m.group(2))})

    sorted_success_loop = sorted(success_loops_each_roles, key=lambda x: (x['success_loop_count']), reverse=True)[:5]
    for e in sorted_success_loop:
        print(e['role'], e['success_loop_count'])
