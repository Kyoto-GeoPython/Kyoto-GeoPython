program main

  implicit none

  integer,parameter::N=10,M=20
  integer::i,j
  real,dimension(1:N,1:M)::x

  open(10,file='filename.out',form='unformatted',access='direct',recl=N*4)

  do i = 1,N
     do j = 1,M
        x(i,j) = i+j*2
     end do
  end do

  do j = 1,M
     write(10,rec=j)(x(i,j),i=1,N)
  end do

  close(10)

end program main
