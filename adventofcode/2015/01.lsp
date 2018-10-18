(defun sol-1 (s)
  (reduce #'+
          (loop for c across s
                collect (cond ((equal c #\() 1) ((equal c #\)) -1) (t 0)))))

(defun sol-2 (s)
  (setf i 0
        n 0)
  (loop for c across s do
        (incf i)
        (setf n (+ n (cond ((equal c #\() 1) ((equal c #\)) -1) (t 0))))
        (if (< n 0) (return i))))

(setf s (read-line))
(print (sol-1 s))
(print (sol-2 s))
