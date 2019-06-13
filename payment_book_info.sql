-- Some payment book related stuff from CIS
-- Migration to CCMS indicated by migrated_flag
SELECT
pb.book_number, 
lr.la_req_no,
lr.la_acc_no_1, lr.la_acc_no_2, lr.la_acc_no_3,
lr.la_apt_ref_no, 
a.full_name,
dso.migrated_flag
FROM
payment_books pb,
applicants a,
la_reqs lr
left outer join dm_suppressed_objects dso
on  lr.la_req_no = dso.identifier
and dso.table_name = 'LA_REQS'
WHERE
pb.payment_acc_req = lr.la_req_no
and a.apt_no = lr.apt_no 
and pb.book_type = 'LAR'
--and lr.la_req_no = 11085964
and pb.date_created > '01-JUN-2017'