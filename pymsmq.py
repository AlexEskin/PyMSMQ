"""pymsmq - The simplest msmq python library"""
from win32com.client import gencache
msmq = gencache.EnsureModule('{D7D6E071-DCCD-11D0-AA4B-0060970DEBAE}', 0, 1, 0)


class Sender(object):
    """docstring for Sender"""
    def __init__(self, PathName):
        super(Sender, self).__init__()

        qi = msmq.MSMQQueueInfo()
        qi.PathName = PathName
        try:
            self.myq = qi.Open(msmq.constants.MQ_SEND_ACCESS,0)
        except:
            qi.Create()
            try:
                self.myq = qi.Open(msmq.constants.MQ_SEND_ACCESS,0)
            except Exception, e:
                raise Exception("Unable to create or oopen msmq "+PathName)            


    def write(self, label, message):
        if self.myq.IsOpen:
            umessage = unicode();
            for i in message:
                umessage+=unichr(ord(i));
            message = umessage

            msg = msmq.MSMQMessage()
            msg.Priority = 4
            msg.Body = message
            msg.Label = label
            msg.Send(self.myq)
        else:
            raise Exception("Queue can't be opened")

    def __del__(self):
        self.myq.Close()
class Reader(object):
    """docstring for Sender"""
    def __init__(self, PathName):
        super(Reader, self).__init__()
        qi = msmq.MSMQQueueInfo()
        qi.PathName = PathName
        self.myq = qi.Open(msmq.constants.MQ_RECEIVE_ACCESS,0)
    def read(self):
        if self.myq.IsOpen:
            msg = self.myq.Receive()
            return msg.Label,msg.Body

    def __del__(self):
        self.myq.Close()