3
��f�  �               @   s  d dl Z d dlZd dlZd dlZe jje�Ze jje�Z	dd� Z
dd� Zdd� Zedk�red	� ed
e	 � x�yhdZx.eed��D ]Zedeef � ejd� q�W ed	� ej� jd d kr�ed
e	 � ned� W qp ek
�r Z zeee� W Y ddZ[X qpX qpW dS )�    Nc             C   sr   t jd|  �j� }|j� }g }xN|D ]F}| |kr$d|kr$|j� d }|j|� td|� �� t jd| � q$W dS )u-   杀死所有与给定进程名匹配的进程zps -axu | grep %sZgrep�   u   杀死进程ID: z
kill -9 %sN)�os�popen�read�
splitlines�split�append�print)Zprocess_nameZos_fileZid_list�infoZfile_id� r   �/tmp/pycharm_project_570/2.py�kill_process
   s    

r   c             C   s�   t jdt � t jdt � t jdt � t jdt � t jdt � d}tj|dd� t| � tjd� td� d| g}tj	|d d d	�}td
� tjd� d S )Nzrm -f %s/wget-log.*zrm -f %s/nohup.outz/usr/bin/killall wget T)�shellr   u   开始执行命令Zpython3)�stdout�stderru   命令已运行�   )
r   r   �current_dir�
subprocess�runr   �time�sleepr	   �Popen)Z	file_path�create_commandZprocessr   r   r   � create_and_detach_screen_session   s    
r   c             C   s�   t jdt � x*td�D ]}dttf }tj|dd� qW xXt jdt �}|j� jdd�}td	|� t	j
d
� t|�| kr<tdt � td� P q<W d S )Nzrm -f %s/soft.txt�   z0nohup python3 %s/zhihu.py 2000 >>  %s/soft.txt &T)r   zcat %s/soft.txt | wc -l�
� u   url生成中，已生成：�   z%s/zhihu.pyu   够了)r   r   r   �ranger   r   r   �replacer	   r   r   �intr   )Znumber�nr   Zline_nur
   r   r   r   �get_url_file*   s    

r"   �__main__i�  z%s/zhihu_down2.pyiX  u8   更新url时间需要等待%d 秒,已等待时间:%d 秒r   �<   u   非整点不重启脚本)r   Zrandomr   r   �path�abspath�__file__Zcurrent_file_path�dirnamer   r   r   r"   �__name__Z
sleep_time�listr   r   r	   Z	localtimeZtm_min�	Exception�er   r   r   r   �<module>   s0   

