      subroutine rungekutta(dt, nend, ret)
        implicit none
        double precision :: dt
        integer :: nend
        double precision :: ret(nend)
Cf2py intent(in) :: dt
Cf2py intent(in)  :: nend
Cf2py intent(out) :: ret
      double precision :: t, p1, p2, p3, p4, u
      integer :: n
      u = 1d0
      do n = 1, nend
        t = dt * real(n)
        p1 = u
        p2 = u + 0.5d0 * dt * p1
        p3 = u + 0.5d0 * dt * p2
        p4 = u + dt * p3
        u = u + dt * 1/6d0 * (p1 + 2 * p2 + 2 * p3 + p4)
        ret(n) = u
      end do
      end subroutine
