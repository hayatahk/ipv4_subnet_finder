USAGE NOTE:


Code 1:
python3 clean_vrf_route.py <input_file>


Note: Replace <input_file> with the path to the file you want to process. The subnets will be saved to proposed-pool.txt. If proposed-pool.txt already exists, the script will show an error and stop without overwriting it.


Code 2:
python3 new_IP_pool.py nooverlap
python3 new_IP_pool.py overlap


Note: The script will generate no-overlap-proposed-pool.txt for “nooverlap” mode and overlapped-subnets.txt for “overlap” mode. Each file will contain the relevant IPs from proposed-pool.txt, listed by their full four octets.


Code 3:
python3 summery_proposed_pool.py <input_file>

Note: Replace <input_file> with the path to the file containing the IP addresses. The results will be saved to summery-proposed-pool.txt, with comments indicating duplicate counts where applicable.
