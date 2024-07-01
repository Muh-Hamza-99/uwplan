import { Trash } from "lucide-react";

type Props = {
  modalId: number;
};

const DeleteTermModal = ({ modalId }: Props) => {
  return (
    <>
        <div className="tooltip" data-tip="Delete term">
            <button className="btn btn-ghost btn-circle" onClick={() => (document.getElementById(`delete-term-modal-${modalId}`) as HTMLDialogElement).showModal()}>
                <Trash />
            </button>
        </div>
        <dialog id={`delete-term-modal-${modalId}`} className="modal modal-bottom sm:modal-middle">
            <div className="modal-box">
                <h3 className="font-bold text-lg">Delete Term</h3>
                <p className="py-4">Delete a term</p>
                <div className="modal-action">
                    <form method="dialog">
                        <button className="btn">Close</button>
                    </form>
                    <button className="btn btn-error">Confirm</button>
                </div>
            </div>
        </dialog>
    </>
  );
};

export default DeleteTermModal;
