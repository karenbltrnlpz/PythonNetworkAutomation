import napalm
from napalm import get_network_driver

# to connect to a network device, we need to import the network driver
# from the napalm library and create a driver object
# specify the device that you are connecting to, in this example Cisco is 'ios'
driver = get_network_driver('ios')

#creating another object
# if you do not want the password hard coded, use the getpass module to retrieve the
# password dynamically

# to pass in the enable password which in this case is cisco
optional_args = {'secret': 'cisco'}

ios = driver('10.1.1.10', 'admin', 'cisco', optional_args=optional_args)

# we open the connection to communicate with the network device
ios.open()

# to check that our connection works, we will print all the methods that
# are offered to us by the ios device

print(dir(ios))

# closing the connection to the device
ios.close()

# '''
# Output of the first router:
#
# C:\Users\belka\PycharmProjects\NetworkAutomation\venv\Scripts\python.exe C:\Users\belka\PycharmProjects\NetworkAutomation\Napalm\napalm_connect.py
# ['__annotations__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_canonical_int', '_check_archive_feature', '_check_file_exists', '_commit_handler', '_create_tmp_file', '_dest_file_system', '_discard_config', '_discover_file_system', '_file_prompt_quiet', '_gen_full_path', '_gen_rollback_cfg', '_get_bgp_route_attr', '_get_pending_commits', '_get_vlan_all_ports', '_get_vlan_from_id', '_get_vrfs', '_inline_tcl_xfer', '_is_vss', '_load_candidate_wrapper', '_netmiko_close', '_netmiko_device', '_netmiko_open', '_normalize_compare_config', '_normalize_merge_diff', '_normalize_merge_diff_incr', '_scp_file', '_send_command', '_send_command_postprocess', '_xfer_file', 'auto_file_prompt', 'auto_rollback_on_error', 'bgp_time_conversion', 'candidate_cfg', 'cli', 'close', 'commit_config', 'compare_config', 'compliance_report', 'config_replace', 'confirm_commit', 'connection_tests', 'dest_file_system', 'device', 'discard_config', 'force_no_enable', 'get_arp_table', 'get_bgp_config', 'get_bgp_neighbors', 'get_bgp_neighbors_detail', 'get_config', 'get_environment', 'get_facts', 'get_firewall_policies', 'get_interfaces', 'get_interfaces_counters', 'get_interfaces_ip', 'get_ipv6_neighbors_table', 'get_lldp_neighbors', 'get_lldp_neighbors_detail', 'get_mac_address_table', 'get_network_instances', 'get_ntp_peers', 'get_ntp_servers', 'get_ntp_stats', 'get_optics', 'get_probes_config', 'get_probes_results', 'get_route_to', 'get_snmp_information', 'get_users', 'get_vlans', 'has_pending_commit', 'hostname', 'inline_transfer', 'is_alive', 'load_merge_candidate', 'load_replace_candidate', 'load_template', 'merge_cfg', 'netmiko_optional_args', 'open', 'parse_uptime', 'password', 'ping', 'platform', 'post_connection_tests', 'pre_connection_tests', 'profile', 'prompt_quiet_changed', 'prompt_quiet_configured', 'rollback', 'rollback_cfg', 'timeout', 'traceroute', 'transport', 'use_canonical_interface', 'username']
#
# Process finished with exit code 0
#
#
# '''