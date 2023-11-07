program intest2
  implicit none
  integer(4) ireadmg, ireadsb
  character(8) subset
  integer(4) lunin,idate,ilat,ilon,iret
  integer(4) ntb,ntmatch,ncx,ncsave,ntread,maxobs,mxtb,nmsg,nmsgmax
  integer(4),allocatable,dimension(:):: nrep,isort,iloc
  character(len=60) :: infile,obstype
  real(8),dimension(8):: hdrdat
  real(8),dimension(2):: hdrdat_test
  real(8),dimension(4):: obsdat
  character(70) hdr,obstr_v1,obstr_v2
  data hdr /'SAID CLATH CLONH YEAR MNTH DAYS HOUR MINU'/
  data obstr_v1 /'HAMD PRLC WDIR WSPD'/ 
  data obstr_v2 /'EHAM PRLC WDIR WSPD'/ 


  lunin=11

  ! Open the test files.
  print *,"START read bufr"

  infile='satwndbufr'
  infile='rrfs.t12z.satwhr.tm00.bufr_d'

  call getcount_bufr(infile,nmsgmax,mxtb)

  open(lunin,file=trim(infile),form='unformatted')
  call openbf(lunin,'IN',lunin)
  call datelen(10)

  ntb=0
  msg_report: do while (ireadmg(lunin,subset,idate) == 0)
     loop_report: do while (ireadsb(lunin) == 0)
        ntb = ntb+1
        maxobs=maxobs+1
!       nrep(nmsg)=nrep(nmsg)+1
!       print*,mxtb
        if (ntb>mxtb) then
           write(6,*)'READ_SATWND: reports exceed maximum ',mxtb
           stop
        endif
        call ufbint(lunin,hdrdat_test,2,1,iret,'CLAT CLON')
        if(abs(hdrdat_test(1))>500.0.and.hdrdat_test(2)>500.0) then
          call ufbint(lunin,hdrdat,8,1,iret,hdr)
          call ufbint(lunin,obsdat,4,1,iret,obstr_v1)
        else
          call ufbint(lunin,hdrdat,8,1,iret,hdr)
          call ufbint(lunin,obsdat,4,1,iret,obstr_v1)
        end if
        if(trim(subset) == 'NC005052' .or. trim(subset) == 'NC005053' .or. trim(subset) == 'NC005054' .or. &  !IR(LW) / CS WV // VIS  GOES-R like winds
           trim(subset) == 'NC005055' .or. trim(subset) == 'NC005056' ) then  
           write(6,'(a8,6f15.2,2f20.2)') trim(subset), hdrdat(1),hdrdat(2),hdrdat(3),hdrdat(4),hdrdat(5),hdrdat(6),obsdat(3),obsdat(4)
        end if
   enddo loop_report
  enddo msg_report

  print *, 'SUCCESS!'
end program intest2

   subroutine  getcount_bufr(inpfile,nmsg,nsub)

!$$$  subprogram documentation block
!  ............................................................
!   subprogram:  getcount         
!   prgmmr:     Woollen, Jack, Su, Xiujuan 
!  abstract:   this subroutine is to read the bufr file to get information on the
!              counts of message and subset.

!  program history log
!  2015-03-27  Su    Modify original code from Jack Woollen

!  input argument list
!     inpfile       - input bufr file

!  output argument list:
!     nmsg         - messge count from input bufr file 
!     nsub         - subset count from input bufr file
!$$$

   implicit none
!  Declare passed variables
   character(len=*)                      ,intent(in ) :: inpfile
   integer(4)                       ,intent(out) :: nmsg,nsub

!  Declare local parameters

   character(len=8)  :: subset
   integer(4)   lunit,ireadmg,nmsub,idate

   lunit=11
   nsub=0;nmsg=0
   open(lunit,file=trim(inpfile),form='unformatted')
   call openbf(lunit,'IN',lunit)
   do while(ireadmg(lunit,subset,idate) >=0)
      nmsg = nmsg+1; nsub = nsub+nmsub(lunit)
   enddo
   call closbf(lunit)

   return
   end
 
