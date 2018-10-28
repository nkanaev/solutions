(ql:quickload "sb-md5")

(defun find-num (h i test)
  (let* ((s (concatenate 'string h (format nil "~S" i)))
         (r (sb-md5:md5sum-string s)))
    (if (funcall test r) i (find-num h (+ i 1) test))))

(defun sol-1 (h)
  (find-num h 0 (lambda (md5) (and (= 0 (elt md5 0))
                                   (= 0 (elt md5 1))
                                   (> 10 (elt md5 2))))))

(defun sol-2 (h)
  (find-num h 0 (lambda (md5) (and (= 0 (elt md5 0))
                                   (= 0 (elt md5 1))
                                   (= 0 (elt md5 2))))))

(setf input "bgvyzdsv")
(print (sol-1 input))
(print (sol-2 input))
